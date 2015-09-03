import os,sys

file = sys.argv[1]

i=0
max_mem=0;
max_line=""

mems=[]

for line in open(file,'r').readlines():
	if i>0:
		x=line.split(',')
		
		if not ( len(x)==5 ): 
			print line
			continue

		mem=0
		try:
			mem = float(x[-1])
			if mem>67e6:
				mems.append('%d %g;\n'%(i,mem))
		except:
			print line
		
		if mem>max_mem:
			max_mem=mem
			max_line=line
	i = i+1

print 	max_mem, max_line

fp=open('c:/temp/mem.log','w')
fp.writelines(mems)
fp.close()
