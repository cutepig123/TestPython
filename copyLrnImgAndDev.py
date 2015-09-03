import os,sys

def	GetBmpFileList(path):
	retfiles = []
	for root, dirs, files in os.walk(path, topdown=False):	
		for name in files:	
			if name.lower().startswith("buffer") and name.lower().endswith(".bmp"):
				fileName=os.path.join(root, name)
				retfiles.append(fileName)
	return retfiles
	
def GetLimitedPath(path, nLim = 50):
	n = len(path)
	
	if n>nLim:
		return path[:nLim/2:] + '...' + path[(n-nLim/2)::]
	else:
		return path
	
def Main():
	path = raw_input("\n\nInput learn folder path:\n")
	files = GetBmpFileList(path)
	assert(len(files)>0)
	
	print '\n\n'
	for i in range(len(files)):
		print i, GetLimitedPath(files[i])
		
	ids=[]
	if len(files)>1:
		ids = raw_input("Pls select file Indexes to copy: (use ' ' to split)")
		ids = [int(x) for x in ids.split()]
		
	dest = int(raw_input("\n\nPls select destination to copy (0:c:\wineagle 1:current learn folder ):"))
	
	dests = ['c:\\wineagle', path]
	
	print '\n\nCreate image.txt'
	fp = open(dests[dest] + "\\images.txt", 'w')
	filesCopy = [files[id] for id in ids]
	for f in filesCopy:
		fp.writelines(f + '\n')
	fp.close()
	
	print '\n\nCopy dev file'
	i = 0
	mapFdr = {}
	for f in filesCopy:
		p1 = f.rfind("tmplDir.")
		assert(p1>0)
		p2 = f.find('\\', p1+1)
		assert(p2>0)
		srcFolder = f[:p2:] + '\\dev\\'
		srcFiles = [srcFolder+'top.dev', srcFolder+'top.dev']
		for src in srcFiles:
			if os.path.isfile(src) and not mapFdr.has_key(src):
				mapFdr[src] = 1
				
				dst = '%s\\dev\\dev%d'%(dests[dest], i)
				i+=1
				
				cmd = 'mkdir ' + dst
				print cmd
				os.system(cmd)
				
				cmd= 'copy %s %s'%(src, dst)
				print cmd
				os.system(cmd)
	
Main()		