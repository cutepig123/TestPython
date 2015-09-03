import os,sys

def intersect(a, b):
	""" return the intersection of two lists """
	return list(set(a) & set(b))
	
#spath, dpath:	Folder path you want to compare
#return:	file name list
	
def GetSameFileList(spath, dpath):
	return ['cmdrpy.log','result.xml','intermed.log']
	
def MySystem(cmd):
	print cmd
	os.system(cmd)
	
#
def Update(spath, dpath):
	print 'spath',spath
	print 'dpath',dpath
	assert(os.path.isdir(spath))
	assert(os.path.isdir(dpath))
	commonFiles =GetSameFileList(spath,dpath)
	print commonFiles
	for fname in commonFiles:
		print
		print fname
		dfilepath ='%s\\%s'%(dpath, fname)
		MySystem( 'move "%s" "%s.bk"'%(dfilepath,dfilepath) )
		sfilepath ='%s\\%s'%(spath, fname)
		MySystem( 'copy "%s" "%s"'%(sfilepath,dfilepath) )

def getValue(line):
	s='<ptyVal>'
	p1 = line.find(s)
	assert(p1>0)
	p1 = p1+len(s)
	
	s='</ptyVal>'
	p2 = line.find(s,p1)
	assert(p2>0)
	
	value = line[p1:p2]
	
	#print value,
	#value = float(value)
	return '<td>%s</td>'%(value)
	
class ItemUpdater:	
	def __init__(self, tdobj):
		self.res = '<td></td>'
		#self.isFound = 0
		self.tdobj = tdobj
		
	def UpdateItem(self, cont):
		#if self.isFound:
		#	return
			
		self.res ='<td></td>'
		p=cont.find('<pty name="%s">'%self.tdobj)
		if p>=0:
			self.res = getValue(cont[p:])
	def GetHdr(self):
		return '<td>%s</td>'%self.tdobj	
		
	def GetResult(self):
		return self.res

def GetAutoRptPath(file):
	fp=open(file,'r')
	conts = ''.join(fp.readlines())
	
	item = ItemUpdater('AutoRpt Path')
	item.UpdateItem(conts)
	return item.GetResult() 
	
def UpdateMain(spath):
	sfile ='%s\\result.xml'%(spath)
	assert(os.path.isfile(sfile))
	dfile =GetAutoRptPath(sfile)
	assert(os.path.isfile(dfile))
	result=r'\result.xml'
	assert(dfile.endswith(result))
	dpath=dfile[:-len(result)]
	Update(spath,dpath)
	
def walkDir(top, callback):
	assert( os.path.isdir(top) )
	for shortName in os.listdir(top):
		fullName =os.path.join(top, shortName)
		print fullName
		if os.path.isfile(fullName) and ( fullName.lower().endswith('.cpp') or fullName.lower().endswith('.c') ):
			print fullName
			callback(top)
			#os.system('pause')
		elif os.path.isdir(fullName): 
			walkDir(fullName)
			
walkDir(sys.argv[1], UpdateMain)
