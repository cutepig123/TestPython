import md5
import sys

#filename=sys.argv[1]
filename='if.py'
print 'Loading Filename:' + filename + '\n'
a=md5.new()
file=open(filename,'rb')
while 1:
    buffer=file.read(65536)
    if len(buffer)>0:
        a.update(buffer)
    else:break
del file
r=a.digest()
s=''
for i in range(0,16):
    t=hex(ord(r[i]))
    if len(t)<4:
        s=s+'0'
    s=s+' '+t[2:]
print s
