import unittest

class KnownValues(unittest.TestCase):
	def testA(self):
		self.assertEqual(1,1)  
	def testB(self):
		x=10
		self.assertEqual(x,1)  
	def testC(self):
		x=1
		self.assertEqual(x,10)  

unittest.main()