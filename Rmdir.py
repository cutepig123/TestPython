import os,sys

def Rmdir(fdr):
	cmd='rmdir /s/q "%s"'%(fdr)
	print cmd
	os.system(cmd)

def Rmdir_rec(top, height):
	if height<3:
		for file in os.listdir(top):
			fullPath=os.path.join(top, file)
			if os.path.isdir(fullPath):
				Rmdir_rec(fullPath, height+1)
	Rmdir(top)

fdr = raw_input("fdr?")
if len(fdr)==0: fdr = '.'

print fdr

Rmdir_rec(fdr,1)