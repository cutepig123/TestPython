import os

file =r'g:\AutoTest\TestScheme\SmokeTest\testSuite.txt'
for line in open(file,'r').readlines():
	line =line.strip()
	if len(line)==0 or line.startswith('#'):
		continue
	print 'Checking',line
	assert( os.path.isdir(line) )
	assert( os.path.isdir(line+r'\learn') )
	playlist =line+r'\playlist.txt'
	assert( os.path.isfile(playlist) )
	
	for case in open(playlist,'r').readlines():
		case =case.strip()
		if len(case)==0 or case.startswith('#'):
			continue
		if(not os.path.isdir(case) ):
			print case, 'not exist!'
			assert(0)