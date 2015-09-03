import os,sys,re

rootpath=r'\\atcex.asmpt.com\ATCFS\VisionTesting\IMAGEDB\ATC\APP\Function\SPI_APP\LoggingCase2D3D\RepeatabilityTestCase\Dynamic\Strip20130904'

frames = [f for f in os.listdir(rootpath) if re.match(r'Frame*', f)]
for frame in frames:
	framepath ='%s\\%s'%(rootpath,frame)
	cases = [f for f in os.listdir(framepath) if re.match(r'LOGI*', f)]
	case = cases[0]
	casepath='%s\\%s'%(framepath,case)
	print casepath
	resultpath='%s\\result.xml'%casepath
	destpath='%s\\%s\\'%(frame,case)
	cmd='xcopy /c/d/e/y %s %s'%(resultpath,destpath)
	print cmd
	os.system(cmd)