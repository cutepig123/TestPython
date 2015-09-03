import os,sys

def ModifyRec(file, rec):
	cont =open(file,'r').read()
	cont =cont.replace('Record ID = 0','Record ID = %d'%rec)
	open(file,'w').write(cont)
	
def mysys(x):
	print x
	os.system(x)
for i in range(23,40):
	ModifyRec('Y:\\SPI\\ASTestBrdTest1\\Learn\\Record\\tmplDir.%.3d\\cmdrpy.log'%i,i)
	#mysys('pause')
	