# countdown.py
#
# A simple generator function

def grab(n):
	for i in range(n):
		print 'submit grab', i
		yield i
		print 'wait grab done', i

# Example use
if __name__ == '__main__':
	for i in grab(10):
		print 'move motor',i+1

