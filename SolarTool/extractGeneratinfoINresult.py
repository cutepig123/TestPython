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
	
	#print value,
	#value = float(value)
	return '<td>%s</td>'%(value)
	
def getFloatValue(line):
	s='<ptyVal>'
	p1 = line.find(s)
	assert(p1>0)
	p1 = p1+len(s)
	
	s='</ptyVal>'
	p2 = line.find(s,p1)
	assert(p2>0)
	
	value = line[p1:p2]
	
	#print value,
	#
	try:
		value = float(value)
	except:
		value = -1
	return value
	
def findMaxAbsData(conts, pty):
	p1=0
	s='<pty name="%s">'%pty
	Roughness=0
	while True:
		p1=conts.find(s,p1)
		if p1>0:
			value = abs( getFloatValue(conts[p1:]) )
			#print 'Roughness Top', value
			#assert( value<=Roughness )
			Roughness = max( value, Roughness )
			p1 = p1 + len(s)
		else:
			break
	return Roughness
	
#InspSinglePair.txt	
def ExtractMinMaxThick( file ):
	fp = open(file,'r')
	conts = ''.join(fp.readlines())
	p1 = conts.find('MinMaxEx:')
	assert(p1>0)
	p2 = conts.find('Min',p1)
	assert(p2>0)
	p3 = conts.find('Max',p2)
	assert(p3>0)
	p4 = conts.find('coOffMin',p3)
	assert(p4>0)
	return '<td>%s</td> <td>%s</td>'%(conts[p2+3:p3],conts[p3+3:p4])

#insp.txt	
def ExtractMinMaxThick2( file ):
	fp = open(file,'r')
	for line in fp.readlines():
		p1 = line.find('Global TTV')
		if(p1>=0):
			return '<td>%s</td>'%(line)
	return 'N.A.'		
	
def getNumCamera():
	return 3
	
def findCameraThick(conts, id):
	s = '<obj type="Camera" idx="%d"><pty name="Average Thickness">'%id
	p = conts.find(s)
	if p<0:
		s = '<obj type="Camera" idx="%d"><pty name="Thickness">'%id
		p = conts.find(s)
	if p<0:
		return '<td></td>'
	return '<td>%g</td>'%getFloatValue(conts[p:-1])
	
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

class CameraThickUpdater:	
	def __init__(self, idx):
		self.res = '<td></td>'
		#self.isFound = 0
		self.idx = idx
		
	def UpdateItem(self, conts):
		self.res = findCameraThick(conts, self.idx)
		
	def GetHdr(self):
		return '<td>Camera%d</td>'%self.idx	
		
	def GetResult(self):
		return self.res
		
items = [ItemUpdater('AutoRpt Path'),ItemUpdater('Status'),ItemUpdater('Average Thickness'),CameraThickUpdater(1),CameraThickUpdater(2),CameraThickUpdater(3),ItemUpdater('TTV'),ItemUpdater('NPointTTV'),ItemUpdater('NPointThick0'),ItemUpdater('NPointThick1'),ItemUpdater('NPointThick2'),ItemUpdater('NPointThick3'),ItemUpdater('NPointThick4'),ItemUpdater('Min Thickness'),ItemUpdater('Max Thickness'),]
items.extend([ItemUpdater('Warpage'),ItemUpdater('BOW'),ItemUpdater('ConstructAndMergeTime'),ItemUpdater('ApplInspTime'),ItemUpdater('TotalInspTime'),ItemUpdater('Roughness'),ItemUpdater('MaxSawMarkDepth'),])
items.extend([ItemUpdater('MaxSawMarkDepthX'),ItemUpdater('MaxSawMarkDepthY'),ItemUpdater('SawMarkOrientation'),ItemUpdater('MaxSawMarkPosX'),ItemUpdater('MaxSawMarkPosY'),ItemUpdater('DenseSawPartitionNum'),ItemUpdater('MaxSawMarkDepth0'),ItemUpdater('MaxSawMarkDepth1'),ItemUpdater('DenseSawWidth')])
			
def processFileresult( dirName, output_file_resultxml ):
	input_file_resultxml=os.path.join(dirName, 'result.xml')
	
	input = '<td>%s</td>'%input_file_resultxml
	#mtime = '<td></td>' 
	mtime = "<td>%s</td>"%time.ctime(os.path.getmtime(input_file_resultxml))

	fp=open(input_file_resultxml,'r')
	fpw=open(output_file_resultxml,'a')
		
	conts = ''.join(fp.readlines())
	
	lines=['<tr>',mtime,input]
	for item in items:
		item.UpdateItem(conts)
		lines.append( item.GetResult() )
	lines.append( "</tr>\n" )
	
	#print lines
	
	fpw.writelines(lines)
	
	fpw.close()
	fp.close()
	
	
def processAll2(top,output_file_resultxml):
	
	print top
	for dir in os.listdir(top):
		dirName=os.path.join(top, dir)
		if not os.path.isdir(dirName):
			continue
		fileName=os.path.join(dirName, 'result.xml')
		if os.path.isfile(fileName):
			print fileName
			processFileresult( dirName, output_file_resultxml )
			
		else:
			
			processAll2(dirName, output_file_resultxml)

def CreateEmptyFile(file, items):
	fpw=open(file,'w')
	
	lines = ["<tr>",'<td>%s</td>'%'mtime','<td>%s</td>'%'input']
	for item in items:
		lines.append( item.GetHdr() )
	lines.append( "</tr>\n" )
	head = '<table name="summary" border="1">'+ ''.join(lines)

	fpw.writelines([ head])
	fpw.close()

input_folder=sys.argv[1]
output_file_resultxml=input_folder+"\\out.htm"


CreateEmptyFile(output_file_resultxml, items)

processAll2(input_folder, output_file_resultxml)
os.system( "start " + output_file_resultxml)
