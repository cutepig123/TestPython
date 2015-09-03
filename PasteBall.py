import sys,os
from opencv import cv
from opencv import highgui
import random

file=sys.argv[1]
rect=cv.cvRect(int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]))
N=int(sys.argv[6])

print 'File', file
print 'Rect', rect.x,rect.y,rect.width,rect.height

print 'N', N

image1=highgui.cvLoadImage(file,0)
image1_c=cv.cvGetSubRect(image1,rect)
destRoi =cv.cvRect(int(sys.argv[7]),int(sys.argv[8]),int(sys.argv[9]),int(sys.argv[10]))

log_file ='\\'.join(file.split('\\')[:-1]) + '\\log.txt'

for i in  range(N):
	image2=cv.cvCloneImage(image1)
	
	dx = int(random.random()*(destRoi.width-rect.width)+439)
	dy =int(random.random()*(destRoi.height-rect.height)+452)
	#print dx,dy
	rect2 =cv.cvRect(dx, dy,rect.width,rect.height)
	image2_c=cv.cvGetSubRect(image2,rect2)
	#print 'Copy'
	cv.cvCopy(image1_c,image2_c)
	
	dest_file ='\\'.join(file.split('\\')[:-1]) + '\\%d.bmp'%i
	print 'dest_offset',rect2.x,rect2.y,'-->',dest_file
	highgui.cvSaveImage(dest_file,image2)


	
