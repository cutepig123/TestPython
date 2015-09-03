import os,sys

#only support folder with name "WISIxxx"
def walkDir(top, fp):
	assert( os.path.isdir(top) )
	for x in os.listdir(top):
		fullName =os.path.join(top, x)
		print fullName
		fileName=os.path.join(fullName, "cmdrpy.log")
		if os.path.isfile(fileName): 
			fp.writelines([fullName+'\n'])
		elif os.path.isdir(fullName): 
			walkDir(fullName,fp)
		
#this version is slow		
def walkDir_old(top, fp):
	i=0
	#copyed_cmdrpy = r"E:\solar_calinsp_20110411\WISI0028\cmdrpy.log"
	#assert( os.path.isfile(copyed_cmdrpy) )
	for root, dirs, files in os.walk(top, topdown=False):	
		for folder in dirs:	
			folderName=os.path.join(root, folder)
			fileName=os.path.join(folderName, "result.xml")
			
			i=i+1
			if i%10==0:
				print folderName
			
			#if not folder.startswith("WISI"): continue
			if not os.path.isfile(fileName): continue
			
			#copy cmdrpy
			#cmd = "copy /y %s %s"%(copyed_cmdrpy, folderName)
			#print cmd
			#os.system(cmd)
			#pause
			
			#gen playlist
			fp.writelines([folderName+'\n'])
				

folder=sys.argv[1]

fp=0
fp = open(folder+"\\playlist.txt","w")
walkDir(folder, fp)
fp.close()
