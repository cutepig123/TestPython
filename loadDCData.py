import os,sys

for i in range(30):
	file =r'\\ahkex\ahkproj\VisionImaging\JSHe\LogCase\Bill\DCLO0005\DCLO0005\EdgeDetect_%d\insp_EdgeList.txt'%i
	print '%',file
	
	for line in open(file,'r').readlines():
		if not line.startswith('Pt_'):
			continue
		p =line.split('=')
		assert(len(p)==2)
		p =p[1].strip()
		print p,
	print
	