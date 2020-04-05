import os,sys

def CompareFolder(fdr1, fdr2):
	F1 =os.listdir(fdr1)
	F2 =os.listdir(fdr2)
	N1 =len(F1)
	N2 =len(F2)
	if not(N1==N2):
		print '[Error]',F1, F2
		assert(0)
		
	F1.sort()
	F2.sort()

	for i in range(len(F1)):
		if not(F1[i]==F2[i]):
			print '[Error]',F1[i],F2[i]
			assert(0)
		C1 =open('%s\\%s'%(fdr1,F1[i]),'r').readlines()
		C2 =open('%s\\%s'%(fdr2,F2[i]),'r').readlines()
		if not( len(C1)==len(C2) ):
			print '[Error]',C1, C2
			assert(0)

		for j in range(len(C1)):
			if not( C1[j]==C2[j] ):
				print j,C1[j],C2[j]
				assert(0)

CompareFolder(sys.argv[1],sys.argv[2])
