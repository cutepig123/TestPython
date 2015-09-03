import os,sys

def MyAssert(x, msg):
	if (not x):
		print msg
		assert(0)
		
def ModifySubset(root,file):
	fileNameSrc=os.path.join(root, file)
	print fileNameSrc
	sim='simulation'
	fileNameDst=os.path.join(root, 'subtest.cfg1')
	fpW = open(fileNameDst,'w')
	folderName=root.split('\\')[-1]
	for line in open(fileNameSrc, 'r').readlines():
		if line.startswith(sim):
			spLine = line.split()
			MyAssert(len(spLine) == 6, "Error line %s\n"%(line))
			#modify 6th to 1
			if(spLine[-1])!='1':
				print '\t0->1'
				spLine[-1] = '1'
			#check 4,5th 's folder name
			s1 = folderName+'\\main.cfg'
			if s1 != spLine[-3]:
				print '\t',spLine[-3], '->', s1
				spLine[-3] = s1
				
			s2 = folderName+'\\trans.cfg'
			if s2 != spLine[-2]:
				print '\t',spLine[-2], '->', s2
				spLine[-2] = s2
			line = ' '.join(spLine) + '\n'
		fpW.writelines([line])
	fpW.close()	
	#print 'ren %s %s_bk'%(fileNameSrc,fileNameSrc)
	if os.path.isfile(fileNameSrc+'bk'):
		os.remove(fileNameSrc+'bk')
	os.rename(fileNameSrc,fileNameSrc+'bk')
	os.rename(fileNameDst,fileNameSrc)
	
def withSpecificExt(name,filters):
	name = name.lower()
	for filter in filters:
		if name.endswith(filter):
			return True
	return False
	
def getFilesInFolder(folder, filters=['subtest.cfg']):
	l=[]
	for root, dirs, files in os.walk(folder):	
		for name in files:	
			if withSpecificExt(name, filters):
				#fileNameSrc=os.path.join(root, name)
				ModifySubset(root, name)
	
getFilesInFolder(sys.argv[1])
