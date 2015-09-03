# Delete everything reachable from the directory named in 'top',
# assuming there are no symbolic links.# CAUTION:  This is dangerous!  For example, if top == '/', it
# could delete all your disk files.
import os

top = '.\'

for root, dirs, files in os.walk(top, topdown=False):	
	for name in files:	
		#os.remove(os.path.join(root, name))	
	for name in dirs:	
		#os.rmdir(os.path.join(root, name))

def TraverseDir(aPath):
	mList = os.listdir(aPath)
	for mPath in mList:
		tPath = os.path.join(aPath,mPath)
		if os.path.isfile(tPath):
			ProcessFile(tPath)
		else :
			TraverseDir(tPath)
