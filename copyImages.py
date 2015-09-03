import os,sys


def walkDir(top):
	
	for root, dirs, files in os.walk(top, topdown=False):	
		for name in files:	
			#os.remove(os.path.join(root, name))	
			fileName=os.path.join(root, name).lower()
			if fileName.endswith('.dll') or fileName.endswith('.lib') or fileName.endswith('.pdb'):
				cmd='move %s %s\\'%(fileName,r'C:\boost_1_44_0\lib')
				print cmd
				os.system(cmd)
				
				
PathJ=sys.argv[1]
walkDir(PathJ)	