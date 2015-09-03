import sys
import myviewtime
#what does this tool can do?
#	read time info from file, the info is identified as "TIME_ID:<int>\n"
#	where TIME_ID is defined in variav\ble : items
#	the tool can find all times associated with TIME_ID defined in "items", and sort the times by order, and output to another file

#init

items = myviewtime.items
#load time info from file
def	LoadData(file):
	global	items
	fp = open(file,'r')
	lines=fp.readlines()
	fp.close()
	times={}
	for item in items:
		times[item]=[]
	for i in range(len(lines)):
		line = lines[i]
		for item in items:	#search each key_word in items[]
			finded=0
			s = item  + ':'
			p=line.find(s)
			#if p>=0:
			if line.startswith(s):
				if i+2>=len(lines): continue
				line = lines[i+1]
				if line.startswith("\tlen:"):
					line = lines[i+2]
					ss="\tmin,median,max:["
					if line.startswith(ss):
						data = line[len(ss):-2:]+' '
						print s,data
						data = [float(i) for i in data.split(',')]
						#print data
						assert(len(data)==3)
						assert(finded==0)
						finded=1
						times[item]=(data)
						#break
	return	times;

def	printDiff(times1, times2, fp):
	global	items
	for timekey in items:	#log each item
		tm1=times1[timekey]
		tm2=times2[timekey]
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