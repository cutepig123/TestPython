import os,sys,datetime

file_in = sys.argv[1]
#fdr_in = os.path.split(file_in)[0]
#if len(fdr_in)==0: fdr_in='.'

dst_folder = file_in+"_"+datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')

fp = open(file_in,'r')
lines = fp.readlines()
fp.close()
IsInComment = 0

os.system('mkdir ' + dst_folder)
os.system('copy /y  "%s" "%s\\"'%(file_in, dst_folder)	)	

fileNum = 1
for line in lines:
	src=line.replace('\r','').replace('\n','').strip()	#delete \r\n
	if len(src) == 0 : continue		#skip empty line
	if src[0] in ['#', ';']:	continue	#skip comment
	
	if src.startswith("/*"):	#partially support /**/ type comment
		IsInComment = 1
		continue
	if IsInComment:
		if src.startswith("*/"):
			IsInComment = 0
		continue
	
	dst=src
	
	p = src.find(':')							#delete x:\
	if p>=0: 
		dst=dst[p+2::]
	else:
		dst = src
		while dst[0]=='\\': dst=dst[1::]
		
	dst = dst_folder + '\\' + dst
	
# continue
	cmd = 'pause'
	if os.path.isdir(src):
		cmd='xcopy /y /e  "%s" "%s\\"'%(src, dst)
		print fileNum,'folder:\t',src,'\n\t',dst
		fileNum += 1
	elif os.path.isfile(src):
		p=dst.rfind('\\')	#del \x
		assert(p>0)
		dst = dst[:(p):]
		#cmd='xcopy /y /e %s %s\\'%(src, dst)	
		if not os.path.isdir(dst):
			cmd='mkdir "%s"' %(dst)
			os.system(cmd)
		cmd='copy /y  "%s" "%s\\"'%(src, dst)	
		print fileNum, 'file:\t',src,'\n\t',dst
		fileNum += 1
	else:
		print "Error:", src, "Not Exist"
	os.system(cmd)
