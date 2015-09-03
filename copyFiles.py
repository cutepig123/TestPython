import os,sys

##Not finished!!!
def CopyFiles(top, destTop):
	for root, dirs, files in os.walk(top, topdown=False):	
		if 1:	
			print root
			print dirs
			print files
			os.system("pause")
			

fromSS = raw_input("from?")
toSS = raw_input("to?")
if len(fromSS)==0: fromSS = '.'
if len(toSS)==0: toSS = '.'

print fromSS
print toSS

#ListDir(fromSS,toSS)#unnecessary!

CopyFiles(fromSS,toSS)