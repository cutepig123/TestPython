import os, sys

def MySystem(s):
	print s
	os.system(s)
	
p=r'Z:\IMAGEDB\APP\Function\SPI\GrabSequence\Test1\LOGI0302'
for i in range(0,10):
	MySystem('move %s\\buffer%.2d.bmp %s\\-buffer%.2d.bmp'%(p,i, p,i+2))
for i in range(10,12):
	MySystem('move %s\\buffer%.2d.bmp %s\\-buffer%.2d.bmp'%(p,i, p,i-10))
	
for i in range(0,12):	
	MySystem('move %s\\-buffer%.2d.bmp %s\\buffer%.2d.bmp'%(p,i, p,i))