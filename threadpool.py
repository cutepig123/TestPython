#!/usr/bin/env python
import Queue
import threading
import urllib2
import time

hosts = ["http://yahoo.com", "http://google.com", "http://amazon.com","http://ibm.com", "http://www.sohu.com"]



class ThreadUrl(threading.Thread):
	"""Threaded Url Grab"""
	def __init__(self, queue):
		threading.Thread.__init__(self)
		self.queue = queue

	def run(self):
		while True:
			#grabs host from queue
			host = self.queue.get()
	
			#grabs urls of hosts and prints first 1024 bytes of page
			url = urllib2.urlopen(host)
			print self.getName() , ':' , url.read(10)
	
			#signals to queue job is done
			self.queue.task_done()

def main():
	queue = Queue.Queue()

	print '#spawn a pool of threads, and pass them queue instance '
	for i in range(5):
		t = ThreadUrl(queue)
		t.setDaemon(True)
		t.start()
		
	print '#populate queue with data'
	for host in hosts:
		queue.put(host)
	
	start = time.time()
	print '#wait on the queue until everything has been processed'
	queue.join()
	print "Elapsed Time: %s" % (time.time() - start)

main()

