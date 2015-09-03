import os,sys,time

def processAll(topPath,file_filter_and_callback):
	#print topPath
	for dir in os.listdir(topPath):
		dirPath=os.path.join(topPath, dir)
		if not os.path.isdir(dirPath):
			continue
		if not file_filter_and_callback(dirPath):
			processAll(dirPath, file_filter_and_callback)
			
g_errFilter=[]

def hasFilter(line,g_errFilter):
	for x in g_errFilter:
		if line.find(x)>=0:
			return 1
	return 0
		
def chkGlmErr(dirPath):
	global g_errFilter
	glmPath=os.path.join(dirPath, 'glm_all.log')
	if not os.path.isfile(glmPath): return 0
	
	if len(g_errFilter)==0:
		g_errFilter =open('glmFilter.txt','r').readlines()
		g_errFilter=[x.strip() for x in g_errFilter]
		print
		print 'Read g_errFilter:', g_errFilter
		print
		
	hasPrintFile =0
	for line in open(glmPath,'r').readlines():
		if line.lower().find('error')>=0:
			if not hasFilter(line, g_errFilter):
				if not hasPrintFile:
					print
					print glmPath
					hasPrintFile=1
				print line.strip()
				
	return 1
	
processAll(r'C:\WinEagle\log',	chkGlmErr)
