import os,sys

path=sys.argv[1]

def CalcThick(file):
	fp=open(file,'r')
	status=-1
	t=[0,0,0,0,0,0]
	thick=[0,0,0]
	for line in fp.readlines():
		if line.startswith('[ RESULT'):
			i=line[len('[ RESULT'):(len('[ RESULT')+1)]
			#print i
			status=int(i)
		elif line.startswith('rNominalH = '):
			t[status]=float(line[len('rNominalH ='):])
	thick[0]=t[3]-t[0]
	thick[1]=t[4]-t[1]
	thick[2]=t[5]-t[2]
	return [t,thick]
	
LD=os.listdir(path)
for casex in LD:
	
	casePath='%s\\%s'%(path,casex)
	print casePath,
	if not (os.path.isdir(casePath)): pass
	
	filePath = '%s\\cmdrpy.log'%(casePath)
	
	if os.path.isfile(filePath):
		#print filePath
		t = CalcThick(filePath)
		print t

	else:
		print

#folder=sys.argv[1]

