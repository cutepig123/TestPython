import os,sys
#count how many lines and characters in defined files

def getFilesInFolder(folder, filters=['.h', '.hpp', '.c', '.cpp']):
	l=[]
	for root, dirs, files in os.walk(folder):	
		for name in files:	
			name = name.lower()
			for filter in filters:
				if name.endswith(filter):
					fileName=os.path.join(root, name)
					l.append(fileName)
	return l
	
def getFileList(file):
	l=[]
	for line in open(file, 'r').readlines():
		line = line.replace('\n','')
		if os.path.isfile(line):
			l.append(line)
		elif os.path.isdir(line):
			for f in getFilesInFolder(line):
				l.append(f)
		else:
			os.system("echo [E] " + line + " >>err.txt")
			
	return l
		
def count(file):
	lines = open(file, 'r').readlines()
	nChar=0
	for line in lines:
		nChar = nChar + len(line)
	return [len(lines), nChar]
	
fileList = []
fileList = getFilesInFolder(sys.argv[1])
#fileList = getFileList("g:\\1.txt")
nLine = 0
nChar = 0
fo = open('g:\\o.htm','w')
fo.writelines(["<table>"])
for file in fileList:
	[nline, nchar] = count(file)
	fo.writelines([ "<tr><td>%s<td>%d<td>%d</tr>" %(file, nline, nchar)])
	nLine = nLine + nline
	nChar = nChar + nchar
	
fo.writelines([ "<tr><td>%s<td>%d<td>%d</tr>" %("Total", nLine, nChar)])
fo.writelines(["</table>"])
fo.close()