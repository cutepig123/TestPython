#coding=utf-8

#Î´Íê³É£¡

import sys

file = '1.exe'

if  len(sys.argv)>1:
	file = sys.argv[1]

f=open(file,'rb')
lines=f.seek()
f.close()