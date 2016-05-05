#!/bin/env python2.7

# Brent Marin and Brad Sherman
# spidey web server

import logging
import getopt
import socket
import sys,os
import signal
import re
import mimetypes

FORK = False
LOGLEVEL = logging.INFO
DOCROOT = '.'
PORT = 9234
ADDRESS  = '0.0.0.0'
PROGRAM  = os.path.basename(sys.argv[0])
BACKLOG = 0

####################################################
# Utility Functions
####################################################

def usage(exit_code=0):
	print '''
	Usage: {program} [-d DOCROOT -p PORT -f -v]
	
	Options:
	-h         Show this help message
	-f         Enable forking mode
	-v         Set logging to DEBUG level

	-d DOCROOT Set root directory (default is current directory)
	-p PORT    TCP Port to listen to (default is 9234)
	'''.format(program=PROGRAM)
	sys.exit(0)

def safe_fork():
	try:
		return os.fork()
	except OSError as e:
		error('Could not fork process: {}'.format(e))


#####################################################
# BaseHandler Class
#####################################################

class BaseHandler(object):
	def __init__(self, fd, address):
		self.logger  = logging.getLogger()        # Grab logging instance
		self.socket  = fd                         # Store socket file descriptor
		self.address = '{}:{}'.format(*address)   # Store address
		self.stream  = self.socket.makefile('w+') # Open file object from file descriptor
		self.debug('Connect')
	
	def debug(self, message, *args):
		message = message.format(*args)
		self.logger.debug('{} | {}'.format(self.address, message))

	def info(self, message, *args):
		message = message.format(*args)
		self.logger.info('{} | {}'.format(self.address, message))

	def warn(self, message, *args):
		message = message.format(*args)
		self.logger.warn('{} | {}'.format(self.address, message))

	def error(self, message, *args):
		message = message.format(*args)
		self.logger.error('{} | {}'.format(self.address, message))

	def exception(self, message, *args):
		message = message.format(*args)
		self.logger.error('{} | {}'.format(self.address, message))

	def handle(self):
		self.debug('Handle')
		raise NotImplementedError

	def finish(self):
		self.debug('Finish')
		try:
			self.stream.flush()
			self.socket.shutdown(socket.SHUT_RDWR)
		except socket.error as e:
			pass    # Ignore socket errors


#####################################################
## HTTP_Handler Class
#####################################################

class HTTP_Handler(BaseHandler):

	def __init__(self,fd,address):
		BaseHandler.__init__(self,fd,address)
		self.request_string = ''
		self.uripath = ''
		self.request_info = []
		self.header_names = []
		self.docroot = DOCROOT
	
	def handle(self):
		try:
			#read all data into request
			data = self.stream.readline()
			while data != '\r\n':
				self.request_string = self.request_string + data
				data = self.stream.readline()

			self.parse_request()
			self.uripath = os.path.normpath(''.join([os.getcwd(), DOCROOT,os.environ['REQUEST_URI']]))

			# Check path existence and types and then dispatch
			absDocroot = os.path.normpath(''.join([os.getcwd(),DOCROOT]))
			if not os.path.exists(self.uripath) or self.uripath.find(absDocroot) != 0:
				print "docroot = " + absDocroot
				print "uripath = " + self.uripath
				self._handle_error(404,'Bad Request') # 404 error
			elif os.path.isfile(self.uripath) and os.access(self.uripath,os.X_OK):
				self._handle_script()   # CGI script
			elif os.path.isfile(self.uripath) and os.access(self.uripath,os.R_OK):
				self._handle_file()     # Static file
			elif os.path.isdir(self.uripath) and os.access(self.uripath,os.R_OK):
				self._handle_directory()# Directory listing
			else:
				self._handle_error(403, 'Forbidden')# 403 error
			
		except socket.error:
			pass    # Ignore socket errors
	
	def parse_request(self):
		#Split request string
		self.request_string = self.request_string.split('\n')[:-1]
		self.request_info = self.request_string[0].split(' ')
		request_headers = self.request_string[1:]
		self.debug('Parsing {}',self.request_info)
		
		#Deal with REQUEST_METHOD, REQUEST_URI, and QUERY_STRING
		method = self.request_info[0]
		uri = self.request_info[1].split("?",1)[0]

		#If there is query string, set it, else, make the query string ''
		try:
			query_string = self.request_info[1].split("?",1)[1]
		except:
			query_string = ''
		
		#Set environment variables
		os.environ['REQUEST_METHOD'] = method
		os.environ['REQUEST_URI'] = uri
		os.environ['QUERY_STRING'] = query_string

		#Parse any headers
		for header in request_headers:
			header = header.split(':',1)
			value = header[1].lstrip()	
			key = header[0]
			key = key.replace('-','_')
			key = key.upper()
			key = 'HTTP_' + key
			self.header_names.append(key)
			os.environ[key] = value
	
	def _handle_directory(self):
		self.debug('Handle Directory')
		self._write_header('text/html')

		#Sort by files and directories, then alphabetically
		contentList = os.listdir(self.uripath)
		dirs = []
		files = []
		for content in contentList:
			if os.path.isfile(''.join([self.uripath,'/',content])):
				files.append(content)
			elif os.path.isdir(''.join([self.uripath,'/',content])):
				dirs.append(content)
		sorted_dirs = sorted(dirs)
		sorted_files = sorted(files)
		contentList = sorted_files + sorted_dirs

		#write and send html
		html = '<h1>Directory Listing: {}</h1>\n<table>\n'.format(os.environ['REQUEST_URI'])
		html = ''.join([html,'<th>Type</th>\n<th>Name</th>\n<th>Size</th>\n'])
		for content in contentList:
			content_path = ''.join([self.uripath,'/',content])
			inode = os.stat(content_path)
			html = ''.join([html,"<tr>\n"])
			if os.path.isdir(content_path):
				html = ''.join([html,"<td>\n","Directory","</td>"])
			elif os.path.isfile(content_path):
				html = ''.join([html,"<td>","File","</td>"])
			html = ''.join([html,"<td> <a href=",os.environ['REQUEST_URI'],content,"/",">",content,"</a> </td>\n"])
			html = ''.join([html,"<td>",str(inode.st_size),"</td>\n"])
			html = ''.join([html,"</tr>\n"])
		html = html + "</table>"

		# add audio
		html = html + '''
			<audio controls autoplay>
				<source src="10StillHere.mp3" type="audio/mpeg">
			</audio>	
		'''
		self.stream.write(html)
#				<source src="horse.ogg" type="audio/ogg">

	def _handle_file(self):	
		self.debug('Handle File')
		mimetype, _ = mimetypes.guess_type(self.uripath)
		if mimetype is None:
	    		mimetype = 'application/octet-stream'
		self._write_header(mimetype)
		fo = open(self.uripath,'rb')
		self.stream.write(fo.read())
		fo.close()
		
	def _handle_script(self):
		self.debug("Handle Script")
		signal.signal(signal.SIGCHLD, signal.SIG_DFL)
		process = os.popen(self.uripath)
		self.stream.write(process.read())
		signal.signal(signal.SIGCHLD,signal.SIG_IGN)

	def _handle_error(self,error_no,message):
		self.logger.debug('HTTP/1.1 {} {}'.format(error_no, message))
		self.stream.write('HTTP/1.1 {} {}\r\n'.format(error_no, message))
		self.stream.write('Content-type: text/html\r\n\r\n')
		self.stream.write('<h1>{} Error</h1>\n'.format(error_no))
		self.stream.write('<img src="http://greyreview.com/wp-content/upload/dailymile-_-404-Not-Found.jpg">')
	
	def _write_header(self,content_type):
		self.stream.write("HTTP/1.0 200 OK\r\nContent-Type: {}\r\n\r\n".format(content_type))


#########################################
## TCPServer Class
#########################################

class TCPServer(object):

	def __init__(self, address=ADDRESS, port=PORT, handler=HTTP_Handler):
		self.logger  = logging.getLogger()                              # Grab logging instance
		self.socket  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# Allocate TCP socket
		self.address = address                                          # Store address to listen on
		self.port    = port                                             # Store port to lisen on
		self.handler = handler                                          # Store handler for incoming connections

	def run(self):
		try:
			# Bind socket to address and port and then listen
			self.socket.bind((self.address, self.port))
			self.socket.listen(BACKLOG)
		except socket.error as e:
			self.logger.error('Could not listen on {}:{}: {}'.format(self.address, self.port, e))
			sys.exit(1)

		self.logger.info('Listening on {}:{}...'.format(self.address, self.port))
		

		#Make init adopt all children
		signal.signal(signal.SIGCHLD,signal.SIG_IGN)
		while True:
			# Accept incoming connection
			client, address = self.socket.accept()
			os.environ['REMOTE_ADDR'] = str(address[0])
			os.environ['REMOTE_HOST'] = str(address[0])
			os.environ['REMOTE_PORT'] = str(address[1])
			self.logger.debug('Accepted connection from {}:{}'.format(*address))
			
			#Forking mode
			if FORK:
				pid = safe_fork()
				#child
				if pid == 0:
					self.process_request(client,address)
					os._exit(0)
				#parent
				else:
					client.close()

			#One process mode
			else:
				self.process_request(client,address)

	def process_request(self,client,address):
		try:
			handler = self.handler(client, address)
			handler.handle()
		except Exception as e:
			handler.exception('Exception: {}', e)
		finally:
			handler.finish()
	
#####################################################
# Main Execution
#####################################################

#parse and error check arguments
try:
	opts, args = getopt.getopt(sys.argv[1:],'hfvd:p:')
except getopt.GetoptError as e:
	print e
	sys.exit()


for opt, val in opts:
	if opt == '-h':
		usage(0)
	elif opt == '-f':
		FORK = True
	elif opt == '-v':
		LOGLEVEL = logging.DEBUG
	elif opt == '-d':
		DOCROOT = str(val);
	elif opt == '-p':
		PORT = int(val);
	else:
		print "Invalid Flag"
		usage(1)

# Set logging level
logging.basicConfig(
	level   = LOGLEVEL,
	format  = '[%(asctime)s] %(message)s',
	datefmt = '%Y-%m-%d %H:%M:%S',
    )

# Instantiate and run server

server = TCPServer(port=PORT)
try:
	server.run()
except KeyboardInterrupt:
	sys.exit(0)




