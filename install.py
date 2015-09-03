import sys,os
from distutils.core import setup, Extension

WARPFILE='__warp__.cpp'
TESTFILE='__test__.py'
CONFFILE='1.conf'
opencv_base_dir = r'D:\Program Files\OpenCV'

def Inst(i_file,ext_name,src_list):
	
	cmd='swig -python -c++ -o ' + WARPFILE + ' ' + i_file
	print '***',cmd
	os.system(cmd)
	
	src_list.append(WARPFILE)
	print '***',ext_name, src_list
	example_module = Extension('_' + (ext_name),
				sources=src_list,
				include_dirs = [os.path.join (opencv_base_dir,
						   'cv', 'include'),
							os.path.join (opencv_base_dir,
							 'cxcore', 'include'),
							 os.path.join (opencv_base_dir,
							 'otherlibs', 'highgui'),
							],
				library_dirs = [os.path.join (opencv_base_dir,
							'lib')],
				libraries = ['cv', 'cxcore','highgui','kernel32','user32','gdi32'],
				)
	setup (name =ext_name,
	   version = '0.1',
	   author	  = "SWIG Docs",
	   description = """Simple swig example from docs""",
	   ext_modules = [example_module],
	   py_modules = [ext_name],
	   
	   )
	   
#extract i_file name,  modulename, src_list
def extractAllInfo(conf_file):
	MSTR='%module'
	
	lines=open(conf_file,'r').readlines()
	print '***reading ' + conf_file
	if len(lines)<2:
		lines = lines[0].split('\r')
		if len(lines)<2:
			assert False
	i_file=lines[0].strip()
	src_list=lines[1].strip().split()
	
	lines=open(i_file,'r').readlines()
	for line in lines:
		line=line.strip()
		if line.find(MSTR)==0:
			module_name=line[len(MSTR)::].strip()
			return [i_file,module_name,src_list]
	assert False #not find module name

def clean(ext_name):
	cmd='del ' + WARPFILE
	print '***',cmd
	os.system(cmd)
	
	cmd='del ' + ext_name + '.py?'
	print '***',cmd
	os.system(cmd)
	
	cmd='rmdir /s /q build\\'
	print '***',cmd
	os.system(cmd)

def test(ext_name):
	f=open(TESTFILE,'w')
	f.writelines(['import ' + ext_name + '\n'] )
	
	f.writelines(['print \'***dir of ' + ext_name + ':\'\n'])
	f.writelines(['for i in dir(' + ext_name + ')'  + ':\n'])
	f.writelines(['\tprint i \n'])
	
	f.writelines(['print \'***dir of ' + ext_name + '._'+ ext_name + ':\'\n'])
	f.writelines(['for i in dir(' + ext_name + '._'+ ext_name +')'  + ':\n'])
	f.writelines(['\tprint i \n'])
	
	f.close()
	os.system(TESTFILE)

def makeConfFile():
	f=open(CONFFILE,'w')
	mList = os.listdir('.')
	line1=''
	line2=''
	for mPath in mList:
		tPath = mPath#os.path.join(aPath,mPath)
		if os.path.isfile(tPath):
			ext = os.path.splitext(tPath)
			if ext[1]=='.c' or ext[1]=='.cpp' or ext[1]=='.cxx':
				line2 += tPath + ' '
			elif ext[1]=='.i':
				line1 = tPath
	f.writelines(['%s\n%s\n' %(line1,line2)])
	f.close()
	
if len(sys.argv)>1 and sys.argv[1]=='mk':
	makeConfFile()

[i_file,ext_name,src_list] = extractAllInfo('1.conf')
print [i_file,ext_name,src_list] 

if len(sys.argv)==1:
	sys.argv.append('all')
print sys.argv[1]

if sys.argv[1]=='all':
	sys.argv[1]='install'
	Inst(i_file,ext_name,src_list)
	clean(ext_name)
	test(ext_name)
elif sys.argv[1]=='clean':
	clean(ext_name)
elif sys.argv[1]=='install' or sys.argv[1]=='build' :
	Inst(i_file,ext_name,src_list)
elif sys.argv[1]=='test':
	test(ext_name)
else:
	print 'do nothing!!'