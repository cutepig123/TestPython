import sys
import myviewtime

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
for item in items:
	times[item]=[]

#process each line	
for line in lines:
	for item in items:	#search each key_word in items[]
		finded=0
		s = '] '+item  + ':'
		p=line.find(s)
		if p>0:
			try:
				data = line[(len(s)+p)::]+' '
				data = float(data)
				times[item].append(data)
				assert(finded==0)
				finded=1
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