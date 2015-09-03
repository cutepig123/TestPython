import os,sys

def	delOtherFolder(path,folder):
	#1st :scan folder
	findedPath=[]
	#print 'start list dir',os.listdir(path),'find',folder
	for mPath in os.listdir(path):
		fullPath=os.path.join(path,mPath)
		if not os.path.isdir(fullPath):continue
		#print 'processing',mPath
		if mPath.lower().find(folder.lower())>=0:
			findedPath.append(fullPath)
			#break
	if len(findedPath)<=0:
		#print 'Cannot find',folder,'in',path
		#return None
		pass
	else:
		#print 'Find',findedPath,'Now del others'
		#2nd, del folder
		for mPath in os.listdir(path):
			fullPath=os.path.join(path,mPath)
			if not os.path.isdir(fullPath):continue
			if mPath.lower().find(folder.lower())<0:
				os.system('rmdir /s /q %s'%(fullPath))
	return findedPath
	
def process_logi(logi_path):
	find = 0
	print 'processing',logi_path,
	Marks=delOtherFolder(logi_path,'mark')
	#print '**',Marks,len(Marks)
	
	for Mark in Marks:
		retrys=delOtherFolder(Mark,'Retry')
		#print '**',retrys,len(retrys)
		for retry in retrys:
			OCRs=delOtherFolder(retry,'ocr')
			#print '**',OCRs,len(OCRs)
			if len(OCRs)>0:
				#print 'find',OCRs
				find=1
	print find
	
print 	'**Del Useless Log Folder Tool(only left ocr logging)**'	
print	'please select action:'
print 	'\t1.current path is AutoRpt*, so I should first del LOGI*'
print 	'\t2.current path is LOGI*, so I should first del Mark'
method=int(raw_input(''))
if method==1:
	for logi in os.listdir('.'):
		if os.path.isdir(logi):
			process_logi(logi)
elif method==2:
	process_logi('.')