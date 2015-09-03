import os,sys,datetime,stat,time

def FileTimeBetweenModifyAndNow(path):
	file_stats = os.stat(path)
	dt = time.time() - file_stats.st_mtime
	print path, dt
	return dt

def Main():	
	file_in = sys.argv[1]
	Mode = {}
	Mode[1] = "Get"
	Mode[2] = "Check out"
	Mode[3] = "Check in"
	#Mode[4] = "Unlock"
	mode = raw_input(Mode)
	mode = int(mode)
	if not Mode.has_key(mode):
		print "Invalid mode:", mode
		exit(0)
		
	versionLabel = raw_input("\n\nInput version label:[Latest Version for get, and Null for put]")
	if len(versionLabel)==0:
		if mode == 1 or mode == 2:
			versionLabel = "Latest Version"
		
	description = ""
	unlockIfLocked = 1
	if mode == 3:
		enhOrBugFs = {}
		enhOrBugFs[0]="Enhancement"
		enhOrBugFs[1]="BugFix"
		enhOrBugF = raw_input(enhOrBugFs)
		enhOrBugF = int(enhOrBugF)
		description = "[%s]%s [Compatibility]Link"%(enhOrBugFs[enhOrBugF], raw_input("\n\npls input description:"))
	if 0 and mode == 2:
		unlockIfLocked_str = raw_input("unlockIfLocked?[0/1] default %d"%unlockIfLocked)
		if len(unlockIfLocked_str)>0:
			unlockIfLocked = int(unlockIfLocked_str)
		
	print
	print		
	print "mode:", Mode[mode]
	print "versionLabel:", versionLabel
	print "description:", description
	os.system("pause")

	dst_folder = "_pvcsGet_"+file_in+"_"+datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')

	fp = open(file_in,'r')
	lines = fp.readlines()
	fp.close()

	print lines

	fileNum = 1
	for line in lines:
		src=line.replace('\r','').replace('\n','').strip()	#delete \r\n
		if len(src) == 0 : continue		#skip empty line
		if src[0] in ['#', ';']:	continue	#skip comment
		
		g_src = src
		dst=src
		
		p = src.find(':')							#delete x:\
		if p>=0: 
			dst=dst[p+2::]
		else:
			assert(0)
			dst = src
			while dst[0]=='\\': dst=dst[1::]
			
		src = dst.replace('\\','/')
		dst = dst_folder + '\\' + dst
		
		#make folder
		if False:
			dstFdr = dst[:dst.rfind('\\'):]
			if not os.path.isdir(dstFdr):
				cmd = 'mkdir "%s"' %dstFdr
				os.system(cmd)

		#get source
		exe = r"\\aaants240.aaaex.asmpt.com\SerenaClnt\vm\win32\bin\pcli "
		userPwd = r' -pr"\\vis\eagleapp" -id"aeejshe:hejinshou" '
		if mode==1:		#get
			cmd= exe + r' Get ' + userPwd + r' -v"%s"  -a"%s" -z /Diebond/%s'%(versionLabel,dst, src)
		elif mode==2:	#check out
			cmd= exe + r' Get ' + userPwd + r' -v"%s" -l -a"%s" -z /Diebond/%s'%(versionLabel,dst, src)
		elif mode==3:	#put, Use default source path
			#check whether file modified
			if 0:
			#if FileTimeBetweenModifyAndNow(g_src)>20*60*60:	#20 minutes
				print '****',fileNum , g_src
				continue
			
			if len(versionLabel)>0:
				cmd= exe + r' Put ' + userPwd + r' -n -v"%s" -m"%s" -z /Diebond/%s'%(versionLabel, description, src)
			else:
				cmd= exe + r' Put ' + userPwd + r' -n -m"%s" -z /Diebond/%s'%(description, src)
		elif mode==4:	#Unlock
			exe2 = r"\\aaants240.aaaex.asmpt.com\SerenaClnt\vm\win32\bin\vcs "
			cmd= exe2 + r' -u  -id"aeejshe:hejinshou" \\vis\eagleapp\Diebond\%s'%(src)
			
		print cmd
		status = os.system(cmd)
		print '****',fileNum , status#, src, dst
		if status<0:
			os.system("pause")
		#if 0:
		#	if mode==2 and unlockIfLocked:	#check out
		#		exe2 = r"\\aaants240.aaaex.asmpt.com\SerenaClnt\vm\win32\bin\vcs "
		#		cmd2= exe2 + r' -u  ' + userPwd + r' -z /Diebond/%s'%(src)
		#		print cmd2
		#		os.system(cmd2)
		#		
		#		os.system(cmd)
		#	os.system("pause")
		fileNum += 1
	os.system('copy %s %s'%(file_in,dst_folder))

Main()		