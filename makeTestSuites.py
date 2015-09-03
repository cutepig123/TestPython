import os

def walkDir(top, fp):
	for root, dirs, files in os.walk(top, topdown=False):	
		for name in files:	
			fileName=os.path.join(root, name)
			fp.writelines([fileName+'\n'])
				
fp = open("testSuites.txt", "w")
walkDir(r"G:\AutoTest\TestScheme\TestSuite", fp)
walkDir(r"G:\AutoTest\TestScheme\SmokeTest", fp)