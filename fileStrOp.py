import os,sys

#Supported Operation:
# -remove [Pattern]
# -replace [old_pattern] [new_pattern]
#Remarks: not support use more than one patterns same time

file =sys.argv[1]
pattern_mode=sys.argv[2]
pattern_mode_int=0
pattern_arg=[]

if pattern_mode=='-remove':
	pattern_arg=sys.argv[3:]
	pattern_mode_int=0
elif pattern_mode=='-replace':
	pattern_arg=sys.argv[3:]
	assert(len(pattern_arg)==2)
	pattern_mode_int=1

print 'pattern_mode_int', pattern_mode_int
print 'pattern_arg', pattern_arg

fpW =open(file+'.new','w')
for line in open(file,'r').readlines():
	if pattern_mode_int==0:
		has_pattern =0
		for pattern in pattern_arg:
			if line.find(pattern)>=0:
				has_pattern=1
				break
		if not has_pattern:
			fpW.write(line)
	elif pattern_mode_int==1:
		s =line.replace(pattern_arg[0],pattern_arg[1])
		fpW.write(s)
fpW.close()	
