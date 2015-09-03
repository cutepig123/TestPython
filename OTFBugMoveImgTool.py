import os,sys

#only support folder with name "WISIxxx"
def MoveImages(caseFdr):
	s='%s\\buffer%02d.bmp'%(caseFdr,3)
	d='%s\\buffer%02d.bmp.1'%(caseFdr,3)
	d2='%s\\done.txt'%(caseFdr)
	if os.path.isfile(d):
		print "File", d, "Exists!ignore"
		print "done.txt", os.path.isfile(d2)
		os.system('pause')
		return
	cmd = 'move \"%s\" \"%s\"'%(s,d)
	print cmd
	os.system(cmd)
	for i in range(3,545+1,6):
		d='%s\\buffer%02d.bmp'%(caseFdr,i)
		s='%s\\buffer%02d.bmp'%(caseFdr,i+6)
		cmd = 'move \"%s\" \"%s\"'%(s,d)
		print cmd
		os.system(cmd)
	os.system('echo done > \"%s\\done.txt\"'%caseFdr)
	#os.system('pause')
	
def walkDir(top):
	i=0
	#assert( os.path.isfile(copyed_cmdrpy) )
	for root, dirs, files in os.walk(top, topdown=True):	
		for folder in dirs:	
			i=i+1
			if i%10==0:
				print root, folder
			
			if not folder.startswith("WISI"): continue
			
			folderName=os.path.join(root, folder)
			MoveImages(folderName)
			
			
				

#folder=sys.argv[1]

folder='\\\\vis_mc_solar\\e\\_3dSolarBk\SawMark1027'
walkDir(folder)

