import os,sys

file=sys.argv[1]
id=int(sys.argv[2])

os.chdir(file)

x='rename buffer%02d.bmp 1.bmp'%id
print x
os.system(x)

x='rename buffer%02d.bmp buffer%02d.bmp'%(id+2,id)
print x
os.system(x)

x='rename 1.bmp buffer%02d.bmp'%(id+2)
print x
os.system(x)
