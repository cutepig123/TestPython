import math,sys

Min = float(sys.argv[1])
Max = float(sys.argv[2])

diff = Max - Min

a=math.log(diff)/math.log(10)
scale_fac = math.floor(a)
scale = pow(10,-scale_fac) 
print a,scale_fac,scale


#Dist =  math.ceil(diff * scale) / scale
Dist = diff

MinScale = math.floor(Min*scale)
Min_Row =  MinScale/scale

MaxScale = math.ceil(Max*scale)
Max_Row =  MaxScale/scale

print Dist,Min_Row,Max_Row