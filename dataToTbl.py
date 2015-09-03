#fw=open(r'C:\My Documents\FreeMat\2.txt','w')
import copy,sys

class MyMap:
	def __init__(self):
		self.data=[]
	def keys(self):
		k=[]
		for i in self.data:
			assert(len(i)==2)
			k.append(i[0])
		return k
		
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
		
ALL=[]
M=MyMap()

inFile=r'C:\My Documents\FreeMat\1.txt'
oFile=r'C:\My Documents\FreeMat\2.txt'
if len(sys.argv)==1:
	print 'Input ouutput not defined, using default!'
else:
	inFile=sys.argv[1]
	oFile=sys.argv[2]
	
print 'inFile', inFile	
print 'oFile', oFile

for line in open(inFile,'r').readlines():
	X=line.split('\t')
	if line.startswith('File'):
		if not M.empty():
			ALL.append(M)
		M=MyMap()
		print 'Read file', X[1].strip()
	if len(X)>1:
		k=X[0].strip()
		v=X[1].strip()
		assert(v.count('\t')==0)
		if k.startswith('MTF Field'):
			M.set(k,v)
			for x in [i.split(':') for i in v.split(',')]:
				M.set(k+'-'+x[0].strip(),x[1].strip())
			
		elif v.startswith('Value measured:'):
			M.set(k,v.split(':')[1].strip())
		elif v.startswith('Magnification ='):
			M.set(k,v.split('=')[1].strip())
		else:
			M.set(k,v)
ALL.append(M)		
print 'Num Data',len(ALL)
#print ALL[0].keys()

for M in ALL:
	for k in ALL[0].keys():
		#print 'i',i,'File:', M.get('File')
		assert( M.get(k) is not None)
		
fw=open(oFile,'w')

T=[x+'\t' for x in ALL[0].keys()]
T.append('\n')
fw.writelines(T)

for M in ALL:
	print 'Handle', M.get('File')
	T=[M.get(x).strip()+'\t' for x in ALL[0].keys()]
	T.append('\n')
	fw.writelines(T)
	
fw.close()
		