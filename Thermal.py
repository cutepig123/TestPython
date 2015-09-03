import os,sys,time

root=sys.argv[1]
for path in os.listdir(root):
	path_f='%s\\%s'%(root,path)
	if not os.path.isdir(path_f):continue
	#print path_f
	f='%s\\buffer00.bmp'%(path_f)
	#print f
	mtime = time.ctime(os.path.getmtime(f))
	mtime = '_'.join(mtime.split())
	mtime = '_'.join(mtime.split(':'))
	for i in range(6):
		f_s='%s\\buffer0%d.bmp'%(path_f,i)
		f_d='%s\\%s_%s_%d.bmp'%(root,mtime,path,i)
		cmd='copy %s %s'%(f_s,f_d)
		print cmd
		os.system(cmd)