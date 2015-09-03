import os

def walkDir(top, fp):
	for root, dirs, files in os.walk(top, topdown=False):	
		for name in files:	
			fileName=os.path.join(root, name)
			fp.writelines(['#'+fileName+'\n'])
			lines = open(fileName, "r").readlines()
			n = len(lines)
			for i in range(0, n, 5):
				fp.writelines([lines[i]+'\n'])
			
				
fp = open("testSuite.txt", "w")
walkDir(r"G:\AutoTest\TestScheme\TestSuite", fp)
walkDir(r"G:\AutoTest\TestScheme\SmokeTest", fp)