import os, sys
import pdb
#gen playlist for autosim
#input: 
# source folder, there is a playlist.txt
# dest folder, there maybe multiple subfolders, each subfolder is generated from source, each case contains buffer00.txt which tells the source case
		
def GetSourceCasePath_old(casepath):
	files =os.listdir(casepath)
	file_name=None
	for file in files:
		if file.startswith('buffer') and file.endswith('.txt'):
			file_name =file
			break
	assert(file_name is not None)
	for line in open('%s\\%s'%(casepath,file_name),'r').readlines():
		if line.startswith('LoadImage   '):
			s =line[len('LoadImage   '):].strip()
			assert s.endswith('.bmp'), s
			s =s[:-len('\\buffer00.bmp')]
			return s
	assert(0)
	return None

# input: autosim generated case folder name (not path name)
# output: the source folder name
def GetSourceCasePath(casename):
	X=casename.split('_')
	assert len(X)>=2, X
	return '_'.join(X[:-1])
	
def TestGetSourceCasePath_old():	
	s =GetSourceCasePath_old(r'A:\Solar3D\AutoSimulation\SingleLooseSmallDeformation\Test1\rot013\WISO0030_rot013')
	print s
	
def TestGetSourceCasePath():	
	s =GetSourceCasePath(r'WISO0030_rot013')
	print s	
 
#input: folder path, it includes a number of cases
#output: return a map, the key is source case name, the dest is the generated case path
def GetSourceCasesPath(cases_path):
	fdrs =os.listdir(cases_path)
	map={}
	for fdr in fdrs:
		#if fdr.startswith('WIS'):
		path ='%s\\%s'%(cases_path,fdr)
		if os.path.isdir(path) and fdr.find('_')>0:
			
			map[GetSourceCasePath(fdr)]=path
	return map
	
def TestGetSourceCasesPath():
	m =GetSourceCasesPath(r'A:\Solar3D\AutoSimulation\SingleLooseSmallDeformation\Test1\rot013')
	print m

#input:	 
#note: the function modifies lines
def write(lines, M1, fp):
	for line in lines:
		line=line.strip()
		X =line.split('\\')
		k=X[-1]
		if not M1.has_key(k):
			print 'No key',k
			fp.writelines(['#' +line +'\n'])
		else:
			line=M1[k]
			fp.writelines([line +'\n'])
		
#support 0 or 1-layer only...
def GetAllSourceCasesPath(s_path, d_path):
	# read source playlist
	fpr =open('%s\\playlist.txt'%s_path,'r')
	Lines =fpr.readlines()
	fpr.close()
	M=GetSourceCasesPath(d_path)
	if len(M)>0:
		fp =open('%s\\playlist.txt'%d_path,'w')
		write(Lines,M,fp)
		fp.close()
	else:
		fp =open('%s\\playlist.txt'%d_path,'w')
		for fdr in os.listdir(d_path):
			if fdr.startswith('learn') or fdr.startswith('.'):
				continue
			path ='%s\\%s'%(d_path,fdr)
			if not os.path.isdir(path):
				continue
			print path,
			M=GetSourceCasesPath(path)
			print len(M), 'Cases'
			if len(M)>0:
				write(Lines,M,fp)
				fp.flush()
				#os.system('pause')
		fp.close()
#TestGetSourceCasesPath()	

def TestGetAllSourceCasesPath():
	#GetAllSourceCasesPath(r'A:\Solar3D\AutoSimulation\source\Test1',r'A:\Solar3D\AutoSimulation\SingleLooseSmallDeformation\Test1\rot013')
	GetAllSourceCasesPath(r'A:\Solar3D\AutoSimulation\source\Test1',r'A:\Solar3D\AutoSimulation\SingleLooseSmallDeformation\Test1')
	
if len(sys.argv)>2:
	GetAllSourceCasesPath(sys.argv[1], sys.argv[2])
else:
	TestGetAllSourceCasesPath()