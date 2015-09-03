import os,sys

def UpdateMain(spath, tail,mpath):
	#print spath
	if spath.endswith(tail):
		print spath
		fp=open(spath,'rb')
		data =fp.read()
		#print data
		fp.close()
		#os.system('pause')
		p =data.find('\r\n\r\n')
		if( p>0):
			data =data[:(p+2)]
		#print data
		#system('pause')
		
		fp=open('%s\\%s'%(mpath,tail),'ab')
		fp.write('path\t%s\n'%spath)
		fp.write(data)
		fp.close()
			
def MywalkDir(top, callback):
	assert( os.path.isdir(top) )
	for shortName in os.listdir(top):
		fullName =os.path.join(top, shortName)
		if os.path.isfile(fullName):
			callback(fullName)
		elif os.path.isdir(fullName): 
			MywalkDir(fullName, callback)
		
mpath= r'Z:\IMAGEDB\APP\Function\RawSolarWafer\Thermal\temp20150408\temp'
if len(sys.argv)>1:	
	mpath =sys.argv[1]
MywalkDir(mpath, lambda file:UpdateMain(file,'SMK_main.xls',mpath))
			
MywalkDir(mpath, lambda file:UpdateMain(file,'Bin.xls',mpath))