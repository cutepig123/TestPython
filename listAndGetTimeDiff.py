import os,sys,datetime,stat,time

SupportedFileExtsList=['c','cpp','h','hpp','vcproj','sln','def','rc']
SupportedFileExtsMap = {}

for ext in SupportedFileExtsList:
	SupportedFileExtsMap[ext]=1

def FormatDt(dt):
	dt = long(dt)
	sec = dt%60
	minu = dt/60
	minute = minu%60
	hour = minu/60
	res="%d:%d:%d"%(hour,minute,sec)
	return res

def FileTimeBetweenModifyAndNow(path):
	file_stats = os.stat(path)
	dt = time.time() - file_stats.st_mtime
	dt = long(dt)
	#print path, time.strftime("%m/%d/%Y %I:%M:%S %p",time.localtime(file_stats[stat.ST_MTIME]))
	return dt

class File:
	def __init__(self, file):
		self.file = file
		self.time = FileTimeBetweenModifyAndNow(file)
	
def ListFilesAndDo(path,resS):
	global SupportedFileExtsMap
	for mPath in os.listdir(path):
		subfullPath=os.path.join(path,mPath)
		if os.path.isdir(subfullPath):
			print subfullPath
			ListFilesAndDo(subfullPath, resS)
		else:
			ext = mPath.split('.')[-1].lower()
			if SupportedFileExtsMap.has_key(ext):
				file = File(subfullPath)
				if file.time<20*60*60:	#10 hours
					resS.append(file)
	return resS

path=sys.argv[1]
Files=[]
ListFilesAndDo(path, Files)
Files.sort(key=lambda f:f.time)
print '**********************'
for f in Files:
	print '%60s%10s'%(f.file, FormatDt(f.time))