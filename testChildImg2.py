import copy
import os,sys
import opencv,  opencv.highgui

def	ChildImg(fileName):
	print fileName
	img = opencv.highgui.cvLoadImage(fileName, 0)
	assert(img.width==2352 and img.height==1728)
	x=(2352-1024)/2
	y=(1728-768)/2
	sumImg = opencv.cv.cvGetSubRect(img, opencv.cv.cvRect(x,y,1024,768) )
	
	fileName2 = fileName + '.1'
	os.rename(fileName,fileName2)
	opencv.highgui.cvSaveImage(fileName, sumImg)
	
def CopyFiles(top):
	for root, dirs, files in os.walk(top, topdown=False):	
		for name in files:	
			if name.endswith('.bmp') and not name.endswith('.bmp.bmp'):
				fileName=os.path.join(root, name)
				ChildImg(fileName)
				
#r'J:\app\User\aeejshe\SPI\case'
CopyFiles(sys.argv[1])
