import threading
import datetime

class ThreadClass(threading.Thread):
	def run(self):
		now = datetime.datetime.now()
		print "%s says Hello World at time: %s" %(self.getName(), now)
		print "%s says Exit" %(self.getName())

for i in range(20):
	t = ThreadClass()
	t.start()
