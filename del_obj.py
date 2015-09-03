import os,sys

fdr = '.\\'
if len(sys.argv)>1:
	fdr=sys.argv[1]
fdr=fdr.strip()
if fdr[-1]!='\\' and fdr[-1]!='/':
	fdr += '\\'

exts=['.obj','.ilk','.ncb','.res','vc70.pdb','.suo','vc70.idb']
for ext in exts:
	cmd='del /f /s /q ' + fdr + '*' + ext
	print '***',cmd
	os.system(cmd)

os.system('pause')