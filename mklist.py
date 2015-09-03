import os,sys

#folder=os.path.abspath('.')
folder = sys.argv[1]

fs = []
for f in os.listdir(folder):
	absf = os.path.join(folder, f)
	if not os.path.isdir(absf):
		continue
	#check the last is number
	nNum = 0
	while absf[-nNum-1].isdigit():
		nNum = nNum+1
	if  nNum==0:
		continue
	
	#check the Lxxxx folder
	if absf[-nNum-1].lower()=='l':
		fs.insert(0,absf)
	else:
		fs.append(absf)

fpW=open(os.path.join(folder, "playlist.txt"),"w")
for l in fs:
	fpW.writelines([l+'\n'])
fpW.close()
