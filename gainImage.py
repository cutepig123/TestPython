import os
from opencv import cv
from opencv import highgui

def Process(inFile, outFile):
	image1 = highgui.cvLoadImage(inFile,0)
	sz = cv.cvGetSize(image1)
	image2 = cv.cvCreateImage(sz, 8, 1)
	cv.cvConvertScale(image1, image2, 1.2, 0)
	highgui.cvSaveImage(outFile, image2)

def main(folder):
	for file in os.listdir(folder):
		print file
		for i in range(4):
			buf = folder+'\\'+file+'\\buffer0%d.bmp'%(i)
			if os.path.isfile(buf):
				Process(buf,buf)
				print buf

folder = raw_input('please input folder:')
main(folder)
