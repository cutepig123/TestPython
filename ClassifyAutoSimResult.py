import os,sys

root =sys.argv[1]
files =os.listdir(root)

def MySystem(s):
	print s
	os.system(s)

#-------------------------------------------------------------------
#classify
for f in files:
	f2 =os.path.join(root, f)
	if not os.path.isdir(f2):
		continue
	f =f.split('_')
	assert(len(f)>0)
	f =f[-1]
	
	dest =os.path.join(root, f)
	if not os.path.isdir(dest):
		MySystem('md %s'%dest)
	MySystem('move %s %s'%(f2,dest))
	
