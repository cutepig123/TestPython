class MyMap:
	def __init__(self):
		self.data=[]
	def keys(self):
		k=[]
		for i in self.data:
			assert(len(i)==2)
			k.append(i[0])
		return k
	def __len__	(self):
		return len(self.data)
		
	def set(self,key,val):
		for i in self.data:
			assert(len(i)==2)
			if i[0]==key:
				i[1]=val
				return
		self.data.append([key,val])
	def get(self,key):
		for i in self.data:
			assert(len(i)==2)
			if i[0]==key:
				return i[1]
		return None
		
	def empty(self):
		return len(self.data)==0
		
	def __repr__(self):
		s=self.data.__repr__()
		return s
		
	