import os,sys


def walkDir(top):
	
	for root, dirs, files in os.walk(top, topdown=False):	
		for name in files:	
			if name == ('green.bmp'):
				fileName=os.path.join(root, name).lower()
				fileNameDest=os.path.join(root, 'buffer00.bmp').lower()
				cmd='move \"%s\" \"%s\"'%(fileName,fileNameDest)
				print cmd
				os.system(cmd)
				
				
PathJ=sys.argv[1]
walkDir(PathJ)	