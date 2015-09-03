import sys

#what does this tool can do?
#	read time info from file, the info is identified as "TIME_ID:<int>\n"
#	where TIME_ID is defined in variav\ble : items
#	the tool can find all times associated with TIME_ID defined in "items", and sort the times by order, and output to another file

#init
infilename='time.txt'
if len(sys.argv)>1:
	infilename=sys.argv[1]
print infilename
fp = open(infilename,'r')
lines=fp.readlines()
fp.close()

times={}
items=[]
for item in items:
	times[item]=[]

#process each line	
for line in lines:
	p1 = line.find(']')
	p2 = line.rfind(':')
	if p1<0 or p2<0 or p1>=p2: continue
	
	item_key = line[(p1+1):p2:]
	item_val = line[(p2+1)::]
	if not times.has_key(item_key):
		times[item_key] = []
		items.append(item_key)
	try:
		item_val = float(item_val)
		times[item_key].append(item_val)
	except Exception,e:
		print 'Exception:',e
		print 'in Line:',line
			#break

#logging			
fpw=open(infilename+'.txt','w')
for timekey in items:	#log each item
	fpw.writelines(timekey+':\n')	
	times[timekey].sort()
	fpw.writelines(str(times[timekey])+'\n')
	#log summary
fpw.writelines('-------------------------summary----------------------------------------\n')
for timekey in items:
	fpw.writelines(timekey+':\n')	
	tm_list=times[timekey]
	n=len(tm_list)
	if n>0:
		tm_list.sort()
		fpw.writelines('\tlen:'+str(n)+'\n')
		fpw.writelines('\tmin,median,max:'+str([tm_list[0],tm_list[n/2],tm_list[-1]])+'\n')
fpw.close()