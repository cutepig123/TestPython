if 0:
	print "Hello, world!"
	import sys
	sys.stdout.write("Hello, world\n")
	for i in sys.path:print i

if 0:
	def buildConnectionString(params):
		"""Build a connection string from a dictionary of parameters.
		Returns string."""
		return ";".join(["%s=%s" % (k, v) for k, v in params.items()])
	if __name__ == "__main__":
		myParams = {"server":"mpilgrim", \
					"database":"master", \
					"uid":"sa", \
					"pwd":"secret" \
					}
		print buildConnectionString(myParams)

if 0:
	length = 5
	breadth = 2
	area = length * breadth
	print 'Area is', area
	print 'Perimeter is', 2 * (length + breadth) 
	
if 0:
	a = '%s=%d' % ('test', 16)
	print a
	
if 1:
	a = [0,0,0]
	a[0]= 'a00'
	a[1:3] = [10, 11]
	a.append(1)
	a.insert(1, 3)
	a.sort()
	a.reverse()
	
	b = [1, 2, 3, 'foo']
	c= [1, 2, 3] + [4, 5, 6]
	print a, b, b[:3], b[1:],c
	