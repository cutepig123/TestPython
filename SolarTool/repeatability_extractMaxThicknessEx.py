import os,sys

def getRange(line):
	p1 = line.find('open_Max_win(this)')
	if (p1<0):
		return 0
	p2= line.find('<td>',p1)
	assert(p2>0)
	p3= line.find('</td>',p2)
	assert(p3>0)
	value = line[p2+len('<td>'):p3]
	
	#print 'AAAAA',value
	value = float(value)
	return value
	
class ItemUpdater:	
	def __init__(self, tdobj):
		self.max_BOW_range = 0
		self.max_BOW_line = '<tr><td>%s</td></tr>'%tdobj
		self.isFound = 0
		self.tdobj = tdobj
		
	def UpdateItem(self, line):
		if self.isFound:
			return
			
		if line.find('<td>%s</td>'%self.tdobj)>=0:
			#print line
			if line.find('<td>-</td>')>=0:
				value = getRange(line)
				print self.tdobj, value
				if value>self.max_BOW_range or not self.isFound:
					self.max_BOW_range = value
					self.max_BOW_line = line
					self.isFound = 1
		#return [max_BOW_range, 		max_BOW_line]
	def GetLine(self):
		#assert(self.isFound)
		return self.max_BOW_line
		
def processFile( input_file, output_file, id ):
	
	
	fpw=open(output_file,'a')
	fpw.writelines([ '%d:<font color=red>%s</font><br>'%(id, input_file ) ])
	
	
	if not os.path.isfile(input_file):
		return
	head = '<table name="summary" border="1"><tr><td>Camera</td><td>Property</td><td>Sample Taken</td><td>Average</td><td>3SD</td><td>Min</td><td>Max</td><td>Range</td><td>Acceptance Range</td><td >Min Directory</td><td ">Max Directory</td></tr><tr style="display : none"><td>MyNumber</td><td>MyNumber</td><td>MyNumber</td><td>MyString</td><td>MyNumber</td><td>MyNumber</td><td>MyNumber</td><td>MyNumber</td><td>MyNumber</td><td>MyNumber</td><td>MyNumber</td><td>MyString</td><td>MyString</td></tr>'
	tail='</table>'
	fpw.writelines([ head])
	
	fp=open(input_file,'r')
	
	#  ## Find max thickness for partition/all
	# ItemUpdater('NPointTTV'),
	items = [ItemUpdater('Status'),ItemUpdater('Average Thickness'), ItemUpdater('Min Thickness'),ItemUpdater('Max Thickness'), ItemUpdater('TTV'),ItemUpdater('NPointTTV'), ItemUpdater('Warpage'), ItemUpdater('BOW'), ItemUpdater('Roughness'),ItemUpdater('WafSz_x') , ]
	items.extend([ItemUpdater('MaxSawMarkDepth'), ItemUpdater('MaxSawMarkCamID'), ItemUpdater('MaxSawMarkPosX'), ItemUpdater('MaxSawMarkPosY'),  ItemUpdater('SumSawMarkDepthX'), ItemUpdater('SumSawMarkDepthY'),ItemUpdater('SawMarkOrientationID')])
	items.extend([ItemUpdater('NPointThick0'),ItemUpdater('NPointThick1'),ItemUpdater('NPointThick2'),ItemUpdater('NPointThick3'),ItemUpdater('NPointThick4'),])
	items.extend([ItemUpdater('MinThickPosX'),ItemUpdater('MinThickPosY'),ItemUpdater('MaxThickPosX'),ItemUpdater('MaxThickPosY')])
	items.extend([ItemUpdater('LineThickMin'),ItemUpdater('LineThickMax'),ItemUpdater('LineTTV'),ItemUpdater('DenseSawWidth')])
	items.extend([ItemUpdater('ConstructAndMergeTime'),ItemUpdater('ApplInspTime'),ItemUpdater('TotalInspTime'),ItemUpdater('DenseSawPartitionNum'),ItemUpdater('MaxSawMarkDepth0'),ItemUpdater('MaxSawMarkDepth1')])
	
	for line in fp.readlines():
		line = line.replace('<td style="display : none">','<td>')
		for item in items:
			item.UpdateItem(line)
	
	lines = []
	for item in items:
		lines.append( item.GetLine() )
	lines.append( tail )
	
	fpw.writelines(lines)
	fpw.close()
	fp.close()

def processAll(top,output_file):
	for root, dirs, files in os.walk(top, topdown=False):	
		for name in files:	
			if name == 'Summary.html':
				fileName=os.path.join(root, name)
				print fileName
				processFile( fileName, output_file,0 )
				
	
def processAll2(top,output_file):
	global id
	
	for dir in os.listdir(top):
		dirName=os.path.join(top, dir)
		
		if not os.path.isdir(dirName):
			continue
		if dir.startswith('WIS'):
			continue
		print 'processing', dirName
		if os.path.isfile(os.path.join(dirName,"Repeatability.log")):
			fileName=os.path.join(dirName, 'Solar Inspection/Summary.html')
			print fileName
			id = id+1
			processFile( fileName, output_file,id )
		else:
			
			processAll2(dirName, output_file)

input_folder=sys.argv[1]
output_file=input_folder+"\\out_repeatibility.htm"
fpw=open(output_file,'w')
fpw.close()
id=0
processAll2(input_folder, output_file)
os.system("start " + output_file)
