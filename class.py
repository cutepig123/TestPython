class CA:
	def test(self):
		print 'CA::test()'

class CB:
	def test(self):
		print 'CB::test()'

class CC(CB,CA):
	pass

c= CC()
c.test()
