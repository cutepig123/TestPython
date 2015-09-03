import os,sys

def intersect(a, b):
	""" return the intersection of two lists """
	return list(set(a) & set(b))
	
#spath, dpath:	Folder path you want to compare
#return:	file name list
def GetSameFileList_old(spath, dpath):
	sList =os.listdir(spath)
	dList =os.listdir(dpath)
	commonFilName= intersect(sList, dList)
	commonFilNameRet =[]
	for fname in commonFilName:
		if fname.lower().endswith('.bmp') or fname.lower().endswith('.tif'):
				continue
		filepath ='%s\\%s'%(spath, fname)
		if os.path.isdir(filepath):
			continue
		commonFilNameRet.append(fname)
	return commonFilNameRet
	
def GetSameFileList(spath, dpath):
	return ['cmdrpy.log','result.xml','intermed.log']
	
def MySystem(cmd):
	print cmd
	os.system(cmd)
#logfile: path of AT_UpdateAllLog.txt
#
def Update(logfile):
	for line in open(logfile,'r').readlines():
		arr =line.split('|')
		spath =arr[0].strip()
		dpath =arr[1].strip()
		print 'spath',spath
		print 'dpath',dpath
		assert(os.path.isdir(spath))
		assert(os.path.isdir(dpath))
		commonFiles =GetSameFileList(spath,dpath)
		print commonFiles
		for fname in commonFiles:
			print
			print fname
			dfilepath ='%s\\%s'%(dpath, fname)
			MySystem( 'move "%s" "%s.bk"'%(dfilepath,dfilepath) )
			sfilepath ='%s\\%s'%(spath, fname)
			MySystem( 'copy "%s" "%s"'%(sfilepath,dfilepath) )
			
Update(sys.argv[1])
