import os,sys

def walkDirX(top, destTop):
	for root, dirs, files in os.walk(top, topdown=False):	
		if 1:	
			fileName=root
			destTopName=os.path.join(destTopName, name)
			cmd='xcopy /y/e %s\\*.cpp %s\\%s'%(fileName,destTop,fileName)
			print cmd
			#os.system(cmd)
						
			cmd='xcopy /y/e %s\\*.c %s\\%s'%(fileName,destTop,fileName)
			print cmd
			#os.system(cmd)

			cmd='xcopy /y/e %s\\*.h %s\\%s'%(fileName,destTop,fileName)
			print cmd
			#os.system(cmd)

def CopyCppHdr(fromS, toS):
	cmd='xcopy /y/e %s\\*.cpp %s\\'%(fromS,toS)
	print cmd
	os.system(cmd)
	cmd='xcopy /y/e %s\\*.c %s\\'%(fromS,toS)
	print cmd
	os.system(cmd)
	cmd='xcopy /y/e %s\\*.h %s\\'%(fromS,toS)
	print cmd
	os.system(cmd)

def ListDir(top, destTop):
	for file in os.listdir(top):
		fullPath=os.path.join(top, file)
		if os.path.isdir(fullPath):
			destfullPath=os.path.join(destTop, file)
			CopyCppHdr(fullPath,destfullPath)
			
fromSS = raw_input("from?")
toSS = raw_input("to?")
if len(fromSS)==0: fromSS = '.'
if len(toSS)==0: toSS = '.'

print fromSS
print toSS

#ListDir(fromSS,toSS)#unnecessary!

CopyCppHdr(fromSS,toSS)