#coding=utf-8

import Queue, threading, sys
from threading import Thread
import time,urllib

# working thread
class Worker(Thread):
	worker_count = 0
	def __init__( self, workQueue, resultQueue, timeout = 0, **kwds):
		Thread.__init__( self, **kwds )
		self.id = Worker.worker_count
		Worker.worker_count += 1
		self.setDaemon( True )
		self.workQueue = workQueue
		self.resultQueue = resultQueue
		self.timeout = timeout

	def run( self ):
		''' the get-some-work, do-some-work main loop of worker threads '''
		while True:
			try:
				callable, args, kwds = self.workQueue.get(timeout=self.timeout)
				res = callable(*args, **kwds)
				print "worker[%2d]: %s" % (self.id, str(res) )
				self.resultQueue.put( res )
			except Queue.Empty:
				break
			except :
				print 'worker[%2d]' % self.id, sys.exc_info()[:2]
				
class WorkerManager:
	def __init__( self, num_of_workers=10, timeout = 1):
		self.workQueue = Queue.Queue()
		self.resultQueue = Queue.Queue()
		self.workers = []
		self.timeout = timeout
		self._recruitThreads( num_of_workers )

	def _recruitThreads( self, num_of_workers ):
		for i in range( num_of_workers ):
			worker = Worker( self.workQueue, self.resultQueue, self.timeout )
			self.workers.append(worker)

	def start(self):
		for w in self.workers:
			w.start()

	def wait_for_complete( self):
		# ...then, wait for each of them to terminate:
		while len(self.workers):
			worker = self.workers.pop()
			worker.join( )
			if worker.isAlive() and not self.workQueue.empty():
				self.workers.append( worker )
		print "All jobs are are completed."

	def add_job( self, callable, *args, **kwds ):
		self.workQueue.put( (callable, args, kwds) )

	def get_result( self, *args, **kwds ):
		return self.resultQueue.get( *args, **kwds )

#Worker类是一个工作线程，不断地从workQueue队列中获取需要执行的任务，执行之，并将结果写入到resultQueue中，这里的 workQueue和resultQueue都是现成安全的，其内部对各个线程的操作做了互斥。当从workQueue中获取任务超时，则线程结束。
#
#WorkerManager负责初始化Worker线程，提供将任务加入队列和获取结果的接口，并能等待所有任务完成。
#
#一个典型的测试例子如下，它用10个线程去下载一个固定页面的内容，实际应用时应该是执行不同的任务。

def test_job(id, sleep = 0.001 ):
	try:
		urllib.urlopen('https://www.sohu.com/').read()
	except:
		print 'exception occur!! jobid=[%4d]' % id, sys.exc_info()[:2]
	return  id

def test():
	import socket
	socket.setdefaulttimeout(10)
	print 'start testing'
	wm = WorkerManager(10)
	for i in range(500):
		wm.add_job( test_job, i, i*0.001 )
	wm.start()
	wm.wait_for_complete()
	print 'end testing'

if __name__ == '__main__':
	test()