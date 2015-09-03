import os,sys

fp =open(sys.argv[1],'r')
Items={}		# One item in new timelog
for line in fp.readlines():
	line=line.strip()
	if len(line)==0:continue
	
	arr =line.split(' ')
	if len(arr)<3: continue
	if len(arr[0])<2: continue
	if not arr[0][0]=='[': continue
	
	thread =arr[0][1:-1]
	name=arr[1]
	time=arr[-1]
	assert(arr[-4]=='Begin' or arr[-4]=='End'), arr
	key ='%s %s'%(thread,name)
		
	if not Items.has_key(key):
		Items[key]=[]
	Items[key].append(time)
	
		
fp.close()

#print Items
for key in Items.keys():
	ks =key.split(' ')
	thread=ks[0]
	name=ks[1]
	v =Items[key]
	if not(len(v)==2):continue
	
	t0 =float(v[0])
	t1 =float(v[1])
	assert(t0<=t1)
	print '%s\t%f\t%f\t%f\t%s : %f\n'%(thread, t0,t1, t1-t0,name, t1)