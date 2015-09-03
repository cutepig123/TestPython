import copy
import shutil
import os,sys
import opencv,  opencv.highgui
import pdb

def	ChildImg(fileName):
	print fileName
	#
	fileName2 = fileName[:-2]
	#pdb.set_trace()
	shutil.copy2(fileName,fileName2)
	img = opencv.highgui.cvLoadImage(fileName2, 0)
	assert(img.width==2352 and img.height==1728)
	x=(2352-1024)/2
	y=(1728-768)/2
	sumImg = opencv.cv.cvGetSubRect(img, opencv.cv.cvRect(x,y,1024,768) )
	
	opencv.highgui.cvSaveImage(fileName2, sumImg)
	
def CopyFiles(top):
	for root, dirs, files in os.walk(top, topdown=False):	
		for name in files:	
			if name.endswith('.bmp.1'):
				fileName=os.path.join(root, name)
				ChildImg(fileName)

#r'J:\app\User\aeejshe\SPI\case'
CopyFiles(sys.argv[1])
