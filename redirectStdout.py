import subprocess,sys

pingPopen = subprocess.Popen(args=sys.argv[1:], shell=True, stdout=subprocess.PIPE)

fp =open ('Log.txt','a')
while 1: 
	x= pingPopen.stdout.readline()
	print x
	
	fp.writelines([x, '\n'])
	fp.flush()
	