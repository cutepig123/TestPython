#coding=utf-8
import string
import sys
#这个文件处理ini

file='Notepad2.ini'
if	len(sys.argv)>1:
	file=sys.argv[1]

lines = open(file).readlines()
hash={}

section=''
for line in lines:
	#delete comments & blanks
	line=line.strip()
	line=line.replace('\n','')

	#i=line.find(';')
	#if i>=0:
	#	line=line[::(i+1)]
	
	if len(line)==0 or line[0]==';':
		continue
	
	#section?
	if line[0]=='[' and line[0]=='[':
		#print 'section:', line[1:-1:]
		section=line[1:-1:].strip()
	else:
		i=line.find('=')
		if i>=0:
			id=line[:i:].strip()
			value=line[(i+1)::].strip()
			#print 'str=',line,'find= @',i
			#print '%30s\t=\t%s' %(id.strip(), value.strip())
			hash[(section,id)]=value
		else:
			print 'Failed!!'

for key in hash.keys():
	print key[0],'|',key[1],'|',hash[key]