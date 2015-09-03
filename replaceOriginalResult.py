import os,sys,time

def getValue(line):
	s='<ptyVal>'
	p1 = line.find(s)
	assert(p1>0)
	p1 = p1+len(s)
	
	s='</ptyVal>'
	p2 = line.find(s,p1)
	assert(p2>0)
	
	value = line[p1:p2]
	
	return '%s'%(value)
	
class ItemUpdater:	
	def __init__(self, tdobj):
		self.res = '<td></td>'
		#self.isFound = 0
		self.tdobj = tdobj
		
	def UpdateItem(self, cont):
		#if self.isFound:
		#	return
			
		p=cont.find('<pty name="%s">'%self.tdobj)
		if p>=0:
			self.res = getValue(cont[p:])
	def GetHdr(self):
		return '<td>%s</td>'%self.tdobj	
		
	def GetResult(self):
		return self.res

	
item = ItemUpdater('AutoRpt Path')

def MySystem(cmd):
	print cmd
	os.system(cmd)

def processFileresult( dirName ):
	input_file_resultxml=os.path.join(dirName, 'result.xml')
	
	#get auto rpt path
	conts = ''.join(open(input_file_resultxml,'r').readlines())
	item.UpdateItem(conts)
	autoRptPath =item.GetResult().strip()
	
	#update
	if len(autoRptPath)>0:
		autoRptRes =os.path.join(autoRptPath, 'result.xml')
		if os.path.isfile(autoRptRes):
			MySystem('move "%s" "%s.1"'%(autoRptRes,autoRptRes))
			MySystem('copy "%s" "%s"'%(input_file_resultxml,autoRptRes))
			
			input=os.path.join(dirName, 'cmdrpy.log')
			output=os.path.join(autoRptPath, 'cmdrpy.log')
			MySystem('move "%s" "%s.1"'%(output,output))
			MySystem('copy "%s" "%s"'%(input,output))
		else:
			print "ERROR, file not exist", autoRptRes
	
def processAll2(top):
	
	print top
	for dir in os.listdir(top):
		dirName=os.path.join(top, dir)
		if not os.path.isdir(dirName):
			continue
		fileName=os.path.join(dirName, 'result.xml')
		if os.path.isfile(fileName):
			print fileName
			processFileresult( dirName )
		else:
			processAll2(dirName)

input_folder=sys.argv[1]
processAll2(input_folder)

