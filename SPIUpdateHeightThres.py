import os,sys

def ModifyRec(file, rec):
	cont =open(file,'r').read()
	cont =cont.replace('Record ID = 26','Record ID = %d'%rec)
	open(file,'w').write(cont)
	
def mysys(x):
	print x
	os.system(x)
for i in range(23,40):
	mysys('xcopy /c/d/e/y Y:\\SPI\\ASTestBrdTest1\\LOGO0059_26 Y:\\SPI\\ASTestBrdTest1\\LOGO0059_%d\\'%i)
	ModifyRec('Y:\\SPI\\ASTestBrdTest1\\LOGO0059_%d\\cmdrpy.log'%i,i)
	#mysys('pause')
	