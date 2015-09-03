import os,sys

f_from = sys.argv[1]
f_to = sys.argv[1]
s = raw_input('source string:')
d = raw_input('dest string:')

fp_from = open(f_from,'r')
fp_to = open(f_to,'w')
print "start!"

for line in fp_from.readlines():
	if line.find('<English>')<0:
		if line.find(s)>=0:
			line = line.replace(s,d)
	print line		
	fp_to.writelines([line])
	
fp_from.close()	
fp_to.close()		