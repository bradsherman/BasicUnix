#!/usr/bin/env python2.7

import work_queue
import json
import sys
import os
import string
import itertools

# Constants
ALPHABET = string.ascii_lowercase + string.digits
PREFIX_LENGTH = 2
HASHES   = 'hashes.txt'
SOURCES  = ('hulk.py', HASHES)
PORT     = 9238
JOURNAL  = {}

# Main execution
if __name__ == '__main__':
	queue = work_queue.WorkQueue(PORT, name='fury-bsherma1',catalog=True)
	queue.specify_log('fury.log')
	
	#Load up Journal if there is one
	if os.path.isfile('journal.json'):
		with open('journal.json') as stream:	
			JOURNAL = json.load(stream)
	
	#One task for passwords of length 1-5
	command = './hulk.py -l {}'.format(6)
	if command in JOURNAL:
		print >>sys.stderr, 'Already did command ',command
	else:
		task = work_queue.Task(command)
		for source in SOURCES:
			task.specify_file(source,source, work_queue.WORK_QUEUE_INPUT)

		queue.submit(task)

	#For longer passwords, make the work less for each task by prefixing
	for i in range(1,PREFIX_LENGTH + 1):
		for prefix in itertools.product(ALPHABET, repeat=i):
			prefix = ''.join(prefix)
			command = './hulk.py -l {} -p {}'.format(6,prefix)
			if command in JOURNAL:
				print >>sys.stderr, 'Already did command ',command
			else:
				task = work_queue.Task(command)
			
				for source in SOURCES:
					task.specify_file(source,source, work_queue.WORK_QUEUE_INPUT)

				queue.submit(task)


	print "All tasks submitted, waiting for responses..."
	while not queue.empty():
		task = queue.wait();
		if task and task.return_status == 0:
			#Add command run and returned ouput to JSON
			JOURNAL[task.command] = task.output.split()
			with open('journal.json.new','w') as stream:
				json.dump(JOURNAL,stream)
			os.rename('journal.json.new','journal.json')	
