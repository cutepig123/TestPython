import os,sys

#only support folder with name "WISIxxx"
#path=r'H:\Renesola\1115_sawrepeatability'
path=sys.argv[1]

NCaseEachWaf=int(sys.argv[2])
NWaf=int(sys.argv[3])

for i in range(1,NWaf+1):
	caseDPath = '%s\\_%02d'%(path,i)
	cmd='mkdir %s'%(caseDPath)
	print 
	print cmd
	os.system(cmd)
	
for i in range(1,NCaseEachWaf+1):
	fdr='%s\\%02d'%(path,i)
	#fdr='%s\\%d'%(path,i)
	j=1
	LD=os.listdir(fdr)
	assert( len(LD)==NWaf )
	for casex in LD:
		
		casePath='%s\\%s'%(fdr,casex)
		print casePath
		assert(os.path.isdir(casePath))
		
		caseDPath = '%s\\_%02d'%(path,j)
	
		if i%2==0:
			caseDPath = '%s\\_%02d'%(path,NWaf+1-j)
		
		cmd='move %s %s'%(casePath,caseDPath)
		print cmd
		os.system(cmd)

		j=j+1
#folder=sys.argv[1]

