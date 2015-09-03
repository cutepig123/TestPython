import os,sys,datetime

def MySystem(cmd):
	print cmd
	os.system(cmd)
	
folder_in = sys.argv[1]
folder_out = sys.argv[2]

#C:\WinEagle\log\AutoRpt\WISI0002_withshift\pair0\top\ProfAfShear_Ref.tif
def CopyCase(folder_in, folder_out):
	MySystem(r'copy /y %s\*.txt %s'%(folder_in,folder_out))
	MySystem(r'copy /y  %s\*.xml %s'%(folder_in,folder_out))
	for i in range(3):
		dest =r'%s\\%d_top.tif'%(folder_out,i)
		if not os.path.isfile(dest):
			MySystem(r'copy /y %s\pair%d\top\ProfAfShear_Ref.tif %s\\%d_top.tif'%(folder_in,i,folder_out,i))
			MySystem(r'copy /y %s\pair%d\btm\ProfAfShear_Ref.tif %s\\%d_btm.tif'%(folder_in,i,folder_out,i))
		
def CopyCases(folder_in, folder_out):
	for file in os.listdir(folder_in):
		filepath ='%s\\%s'%(folder_in, file)
		
		if os.path.isdir(filepath) and file.lower().startswith('wisi'):
			destpath ='%s\\%s'%(folder_out, file)
			MySystem(r'mkdir "%s"'%(destpath))
			CopyCase(filepath, destpath)
			
CopyCases(folder_in, folder_out)		
