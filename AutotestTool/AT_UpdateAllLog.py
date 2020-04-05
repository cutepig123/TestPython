import os,sys
from util import intersect
from util import MySystem
	
def GetSameFileList(spath, dpath):
	return ['cmdrpy.log','result.xml','intermed.log']
	

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
