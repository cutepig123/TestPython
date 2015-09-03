import os

#mapType can be "net use " or "subst "
#drive look like "c:"
def	IsMapped(mapType,drive):
	print '>>>',mapType
	pp = os.popen(mapType)
	cmdRpy = pp.read()
	print cmdRpy
	pp.close()
	return cmdRpy.lower().find(driveL.lower())>=0
	
fp = open("netpath.txt","r")
lines=fp.readlines()
fp.close()

for line in lines:
	if line[-1]=='\n':	#del '\n'
		line = line[:-1:]
	line = line.strip()	#ignore blanks @start & end
	if len(line)==0 or line[0] == '#' :	#ignore comment
		continue
	data = line.split()
	if len(data) != 2:
		print "!=2,",line
		continue
	driveL = data[0]
	driveR = data[1]
	print '*****',line
	
	#delete driveL
	if IsMapped("net use", driveL):
		cmd = "net use %s /d " %(driveL)
		print '>>>',cmd
		os.system(cmd)
	if IsMapped("subst", driveL):
		cmd = "subst %s /d " %(driveL)
		print '>>>',cmd
		os.system(cmd)
		
	#map driveL
	if driveR[0] == '\\':
		cmd = "net use %s %s " %(driveL, driveR)
		print '>>>',cmd
		os.system(cmd)
		cmd = "net use "
	else:
		cmd = "subst %s %s " %(driveL, driveR)
		print '>>>',cmd
		os.system(cmd)
		cmd = "subst "
	
	#check status
	if IsMapped(cmd,driveL):
		print "OK"
	else:
		print line, "FAIL"
		os.system("pause")
	
	