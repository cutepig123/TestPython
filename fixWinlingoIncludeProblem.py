import os,sys

def getIncludeIdx(cpp_file, header_file):
	i=0
	for line in open(cpp_file).readlines():
		if not line.startswith('#include'):
			continue
		i=i+1
		if header_file.lower() in line.lower():
			return i
	return i
	
def correctWinlingo(cpp_file):
	cmd ='copy /y "%s" "%s.1"'%(cpp_file,cpp_file)
	print cmd
	os.system(cmd)
	
	
	lines =open('%s.1'%cpp_file).readlines()
	
	#find the 1st include of 
	inc_1st_line =-1
	inc_stdafx =-1
	i=0
	for line in lines:
		if line.startswith('#include'):
			if inc_1st_line<0:
				inc_1st_line =i
			if 'stdafx.h'.lower() in line.lower():
				assert(inc_stdafx<0)
				inc_stdafx =i
		i =i+1
		
	assert( inc_1st_line<inc_stdafx )
	t =lines[inc_stdafx]
	lines[inc_stdafx] =lines[inc_1st_line]
	lines[inc_1st_line] =t
	
	fpw =open(cpp_file,'w')
	fpw.writelines(lines)
	fpw.close()
	
	os.system('pause')
	
def Log(x):
	fp =open('1.txt','a')
	print >>fp, x
	fp.close()
	
def replace(file):
	stdafxidx =getIncludeIdx(file,'stdafx.h')
	lingoidx =getIncludeIdx(file,'winlingo.h')
	if stdafxidx>lingoidx:
		Log(file)
		correctWinlingo(file)
		
def walkDir(top):
	assert( os.path.isdir(top) )
	for shortName in os.listdir(top):
		fullName =os.path.join(top, shortName)
		print fullName
		if os.path.isfile(fullName) and ( fullName.lower().endswith('.cpp') or fullName.lower().endswith('.c') ):
			print fullName
			
			replace(fullName)
			
			#os.system('pause')
		elif os.path.isdir(fullName): 
			walkDir(fullName)
			
folder=sys.argv[1]
walkDir(folder)
