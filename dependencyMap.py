import os

def GetInclFile(line):
	line = line.strip()
	incl = "include"
	if len(line)<len(incl)+3:
		return None
	if line[0]!='#':
		return None
		
	line = line[1:].strip()
	if len(line)<len(incl)+2:
		return None
	if not line.startswith(incl):
		return None
		
	line = line[len(incl):].strip()
	if len(line)<=2:
		return None
	if line.startswith('<') and line.endswith('>'):
		return line[1:-1]
	if line.startswith('"') and line.endswith('"'):
		return line[1:-1]
	return None

def FindAllDependency(file):
	print file
	res=[]
	for line in open(file,"r").readlines():
		incl = GetInclFile(line)
		if incl is not None:
			print '\t',incl
			res.append(incl)

def FindAllDependency_folder_bug(folder):
	for file in os.listdir(folder):
		filePatjh = os.path.join(folder,file)
		if os.path.isfile(filePatjh):
			FindAllDependency(filePatjh)
			
def FindAllDependency_folder(folder):
	for root, dirs, files in os.walk(folder, topdown=False):
		filePatjh = os.path.join(root,files)
		FindAllDependency(filePatjh)
			
FindAllDependency_folder_bug(r'C:\MyProjectOO\AsmVision\Imaging')