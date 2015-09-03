import sys

if len(sys.argv)>6:
	x1 = int(sys.argv[1])
	y1 = int(sys.argv[2])
	x2 = int(sys.argv[3])
	y2 = int(sys.argv[4])
	w = int(sys.argv[5])
	h = int(sys.argv[6])
else:
	x1 = int(raw_input('left top x'))
	y1 = int(raw_input('left top y'))
	x2 = int(raw_input('rb x'))
	y2 = int(raw_input('rb y'))
	w=512
	h=512
	
exp_mag = 1#float(raw_input("Input magnification:"))
x1 *= exp_mag
y1 *= exp_mag
x2 *= exp_mag
y2 *= exp_mag
#w *= exp_mag
#h *= exp_mag
w=0
h=0

p1=[x2-w/2, y1-h/2]	#right top 
p2=[x1-w/2, y1-h/2]	#left top
p3=[x1-w/2, y2-h/2]	#left bottom
p4=[x2-w/2, y2-h/2]	#right bottom

allpt=[p1,p2,p3,p4,p1]

print 'UL =', p2[0], p2[1]
print 'LR =', p4[0], p4[1]

i=1
for p in allpt:
	#print "Corner" , i ,"=" , p[0],",", p[1], ",",p[0],",", p[1], ",",p[0],",", p[1]
	print "Pt%d.pt"%i , "=" , p[0],",", p[1]
	i+=1