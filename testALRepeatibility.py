import copy
import os,sys
import opencv,  opencv.highgui

		
def	ComputeSDAndAvg(fileName, x,y,w,h):
	img = opencv.highgui.cvLoadImage(fileName, 0)
	sumImg = opencv.cv.cvGetSubRect(img, opencv.cv.cvRect(x,y,w,h) )
	avg = opencv.cv.cvAvg(sumImg)
	mean = opencv.cv.cvScalar(0) 
	std_dev = opencv.cv.cvScalar(0) 
	opencv.cv.cvAvgSdv(sumImg, mean, std_dev)
	
	#Modify image
	img = opencv.highgui.cvLoadImage(fileName, 1)
	opencv.cv.cvRectangle(img, opencv.cv.cvPoint(x,y),opencv.cv.cvPoint(x+w,y+h),opencv.cv.cvScalar(0,0,255))
	fileNameOut = fileName + '.jpg'
	opencv.highgui.cvSaveImage(fileNameOut, img)
	#return [fileNameOut, avg[0] ]
	return [fileNameOut, avg[0] , mean[0], std_dev[0]]	# Note: avg == mean

def Cmp(x,y):
	a=x[1]
	b=y[1]
	if a>b:
		return 1
	if a<b:
		return -1;
	return 0
	
def	PrintHtml(result,fileName):
	fp = open(fileName, "w")
	
	fp.write( '<font color=red>===Image compare tool report===</font><br>\n' )
	#compute Min-Max avg
	a=copy.deepcopy(result)
	a.sort(Cmp)
	#print a
	fp.write( 'avg MIN %f MAX %f DIFF %f <br>\n' %(a[0][1], a[-1][1], -a[0][1] + a[-1][1]) )
	
	#print table
	fp.write( '<table border=1>\n' )
	fp.write( '<tr><td>Image</td><td>Avg</td><td>SD</td></tr>\n' )
	for res in result:
		fp.write( '<tr><td> <img  width=400 height=400 src=%s > </td><td>%f,%f</td><td>%f</td></tr>\n' %(res[0], res[1], res[2], res[3]) )
	fp.write( '</table>\n' )
	fp.close()
	
top = r'C:\WinEagle\log\other'
mode = 1	#0 AutoLight repeatiblity, 1 one ROI mode
result = []
xywh=[1,1,100,100]
if len(sys.argv)>=5:
	xywh = [ int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])]
else:
	print "Using default ROI"
	
if mode == 0:
	if len(sys.argv)>=6:
		imagePath = sys.argv[5]
		pos = imagePath.rfind('\\LGT')
		if pos>0: 
			top = imagePath[:pos:]
		else:
			print 'Invalid image path, cannot find LGT logging folder'
			assert(0)
	else:
		print "Using default path"	
	print 'Path:', top

	i=0
	for root, dirs, files in os.walk(top, topdown=True):	

		for name in files:	
			lName = name.lower()
			if lName.endswith('_c0.bmp') and lName.startswith('c_') and root.split('\\')[-1].startswith('cntL'):
				fullPath = os.path.join(root, name)
				i += 1
				print i,
				if len(fullPath)>60:
					print fullPath[:10] + '...' +fullPath[-50:]
				else:
					print fullPath
				[fileNameOut, avg, mean, std_dev ]= ComputeSDAndAvg(fullPath, xywh[0], xywh[1], xywh[2], xywh[3])
				result.append([fileNameOut, avg, mean, std_dev ])
			
		for name in dirs:	
			#os.rmdir(os.path.join(root, name))
			pass
	htmlFile = os.path.join(top, 'result.html')		
	print htmlFile
	PrintHtml(result, htmlFile)
	os.system('explorer.exe "%s"' %htmlFile)
else:
	fullPath = sys.argv[5]
	[fileNameOut, avg, mean, std_dev ]= ComputeSDAndAvg(fullPath, xywh[0], xywh[1], xywh[2], xywh[3])
	print "File:", fileNameOut
	print "avg:", avg
	print "SD:", std_dev
