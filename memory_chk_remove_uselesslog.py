import os,sys

fin =open(sys.argv[1],'r')
fou=open(sys.argv[1]+'.log','w')

last_memo =0
for line in fin.readlines():
	array =line.strip().split(',')
	if len(array)!=5:
		print 'Error:',line
	else:	
		try:
			cur_mem =float(line[3]) +float(line[4])
			if cur_mem-last_memo>1000000:
				fou.writes([line])
			last_memo =cur_mem
		except:
			print 'Crash:', line
fin.close()
fou.close()
