import os

os.system(r'move c:\wineagle\playlist.txt c:\wineagle\playlist1.txt')
lines = open(r"c:\wineagle\playlist1.txt","r").readlines()
numLines=len(lines)
numLinesToRead=10
step=1
if numLines>numLinesToRead:
	step = numLines/numLinesToRead
	
fpw=open(r"c:\wineagle\playlist.txt","w")	
for i in range(0,numLines-1,step):
	#print i
	fpw.write(lines[i]);
fpw.close()	
