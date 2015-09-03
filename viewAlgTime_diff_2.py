import sys
#what does this tool can do?
#	read time info from file, the info is identified as "TIME_ID:<int>\n"
#	where TIME_ID is defined in variav\ble : items
#	the tool can find all times associated with TIME_ID defined in "items", and sort the times by order, and output to another file

#init

items = []
items_dic={}
#load time info from file
def	LoadData(file):
	global	items,items_dic
	fp = open(file,'r')
	lines=fp.readlines()
	fp.close()
	times={}
	
	status=0
	i=0
	while i<len(lines):
		line = lines[i]
		#print '***',line
		if status==0:
			if line.find('----summary--------')>=0: 
				status=1
			i=i+1
		elif status==1:
			if not line.endswith(':\n'):
				i=i+1
				continue
			item_key = line[:-2:]
			#print '---',item_key
			
			if i+2>=len(lines): 
				#print 'end..'
				break
				
			line = lines[i+1]
			if (line.startswith("\tlen:")):
				line = lines[i+2]
				ss="\tmin,median,max:["
				if (line.startswith(ss)):
					
					data = line[len(ss):-2:]+' '
					#print '|||',data
					data = [float(j) for j in data.split(',')]
					print '---',item_key,data
					assert(len(data)==3)
					times[item_key]=(data)
					if not items_dic.has_key(item_key):
						items_dic[item_key]=1
						items.append(item_key)
			
			i=i+1
			
	return	times;

def	printDiff(times1, times2, fp):
	global	items
	for timekey in items:	#log each item
		if times1.has_key(timekey):
			tm1=times1[timekey]
		else:
			tm1=[]
			
		if times2.has_key(timekey):
			tm2=times2[timekey]
		else:
			tm2=[]
			
		fp.writelines([timekey+':\n', '\ttm1:'+str(tm1)+'\n', '\ttm2:'+str(tm2)+'\n'])
		if len(tm1)==3 and len(tm2)==3:
			tmdiff = [tm1[i]-tm2[i] for i in range(3)]
			fp.writelines(['\ttmDiff:'+str(tmdiff)+'\n'])
			

	
file1=sys.argv[1]
file2=sys.argv[2]
times1 = LoadData(file1)
times2 = LoadData(file2)

fpw=open(file1+file2+'.txt','w')
printDiff(times1, times2, fpw)
fpw.close()