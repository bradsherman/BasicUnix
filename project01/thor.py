#!/usr/bin/env python2.7

# Brad Sherman and Brent Marin
# Project 01

import os
import sys
import socket
import getopt
import logging
import time

ADDRESS   = '127.0.0.1'
PORT      = 80
PROGNAME  = os.path.basename(sys.argv[0])
REQUESTS  = 1
PROCESSES = 1
LOGLEVEL  = logging.INFO

def usage(exit_code=0):
	print >>sys.stderr, '''Usage: {program} [-r REQUESTS -p PROCESSES -v ] URL
	Options:
		-h             Show this help message
		-v             Set logging level to DEBUG
		
		-r REQUESTS    Number of requests per process (default = 1)
		-p PROCESSES   Number of processes (default = 1)'''.format(program=PROGNAME)
	sys.exit(exit_code)

class TCPClient(object):
	def __init__(self,address=ADDRESS,port=PORT):
		# Make TCP client with given address and port
		self.logger  = logging.getLogger()			                   # logging instance
		self.socket  = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # Allocate TCP Socket
		# Lookup host address
		try:
			self.address = socket.gethostbyname(address)
			self.port = port
		except socket.gaierror as e:
			logging.error('Unable to lookup {}: {}'.format(address,e))
			sys.exit(1)
		#self.port    = port

	def handle(self):
		# Handle the connection
		self.logger.debug('Handle')
		raise NotImplementedError

	def run(self):
		# Run by connecting to address and port and executing handle function
		try:
			self.socket.connect((self.address,self.port))
			self.stream = self.socket.makefile('w+')
		except socket.error as e:
			self.logger.error('Could not connect to {}:{}: {}'.format(self.address,self.port,e))
			sys.exit(1)

		self.logger.debug('Connected to {}:{}...'.format(self.address,self.port))

		# Run handle and then finish method
		try:
			self.handle()
		except Exception as e:
			self.logger.exception('Exception: {}'.format(e))
		finally:
			self.finish()

	def finish(self):
		# finish connection
		self.logger.debug('Finish')
		try:
			self.socket.shutdown(socket.SHUT_RDWR)
		except socket.error:
			pass
		finally:
			self.socket.close()

class HTTPClient(TCPClient):
	def __init__(self,url):
		self.url = url.split('://')[-1]
		self.port = 80
		ADDRESS = self.url.split('/')[0]
		QUERY = ''
		if '/' not in self.url:
			self.path = '/'
			ADDRESS = self.url.split(':')[0]
			if ':' in self.url:
				self.port = int(self.url.split(':')[1])
		else:
			self.path = '/' + self.url.split('/',1)[-1]	
			if '?' in self.url:
				self.path = self.path.split('?')[0]
			if ':' in self.url:
				self.port = self.url.split(':')[1]
				self.port = int(self.port.split('/')[0])
				ADDRESS = self.url.split(':')[0]

		if '?' in self.url:
			QUERY = self.url.split('?')[-1]

		self.host = ADDRESS
#		print self.host
#		print self.port
#		print self.path

		TCPClient.__init__(self,self.host,self.port)
		self.logger.debug('URL: {}'.format(url))
		self.logger.debug('HOST: {}'.format(self.host))
		self.logger.debug('PORT: {}'.format(self.port))
		self.logger.debug('PATH: {}'.format(self.path))

	def handle(self):
		# Read data and write it out until EOF
		self.logger.debug('Handle')

		try:
			self.logger.debug('Sending request...')
			self.stream.write('GET {} HTTP/1.0\r\n'.format(self.path))
			self.stream.write('Host: {}\r\n'.format(self.host))
			self.stream.write('\r\n')
			self.stream.flush()

			self.logger.debug('Receiving response...')
			data = self.stream.readline()
			while data:
				sys.stdout.write(data)
				data = self.stream.readline()
				
		except socket.error:
			pass

# Main
if __name__ == '__main__':
	try:
		options,arguments = getopt.getopt(sys.argv[1:],"hvr:p:")
	except getopt.GetoptError as e:
		usage(1)

	for opt, arg in options:
		if opt == '-v':
			LOGLEVEL = logging.DEBUG
		elif opt == '-r':
			REQUESTS = arg
		elif opt == '-p':
			PROCESSES = arg
		else:
			usage(1)
	
	if len(arguments) >= 1:
		URL = arguments[0]
	else:
		usage(1)

	# Set log level
	logging.basicConfig(
			level    = LOGLEVEL,
			format   = '[%(asctime)s] %(message)s',
			datefmt  = '%Y-%m-%d %H:%M:%S',
			)


	# Instantiate and run client
	for process in range(int(PROCESSES)):
		total_time = 0
		try:
			logging.debug('Forking...')
			pid = os.fork()
			if pid == 0:
				for request in range(int(REQUESTS)):
					start_time = time.time()
					client = HTTPClient(URL)
					try:
						client.run()
						end_time = time.time()
						total_time = total_time + (end_time - start_time)
						logging.debug('{} | Elapsed time: {:0.2f}'.format(os.getpid(),end_time - start_time))
					except KeyboardInterrupt:
						os._exit(0)
				logging.debug('{} | Average elapsed time: {:0.2f}'.format(os.getpid(),total_time/int(REQUESTS)))
				os._exit(0)
			else:
				pass
		except OSError as e:
			print 'Could not fork: {}'.format(e)
	for wait in range(int(PROCESSES)):
		logging.debug('Waiting...')
		pid,status = os.wait()
		logging.debug('Process {} terminated with exit status {}'.format(pid,status))
	
