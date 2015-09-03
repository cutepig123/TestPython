import os,sys

def resetValue(line ):
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
	return line[:p1] + '0' +line[p2:]
	
def ReplaceUnitID( input_file_resultxml ):
	os.system('move %s %s.1'%(input_file_resultxml,input_file_resultxml))
	fp=open('%s.1'%input_file_resultxml,'r')
	conts = fp.read()
	fp.close()
	
	unitId=""
	s='<pty name="Unit ID">'
	p1=conts.find(s)
	assert (p1>0)
	conts2 = conts[:p1] + resetValue(conts[p1:])
	fp=open('%s'%input_file_resultxml,'w')
	fp.write(conts2)
	fp.close()
	
def processAll2(top, F):
	for dir in os.listdir(top):
		dirName=os.path.join(top, dir)
		if not os.path.isdir(dirName):
			continue
		if dir.startswith('WIS'):
			fileName=os.path.join(dirName, 'result.xml')
			if not os.path.isfile(fileName):
				continue
			print fileName
			F(fileName)
		else:
			processAll2(dirName,  F)
			
processAll2(sys.argv[1],ReplaceUnitID)
