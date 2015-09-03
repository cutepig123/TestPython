#coding=utf-8

#有一个文件，每一行有一个英文单词，打印出文件所有互为反序的单词（反序的定义：比?
#第三行 是dog,第八行是god,则dog与god是反序的）。
#
#不用做, 我搞错了, 以为是输出所有的重排
#只是逆序的话,一个hash就够了, 每次读入一个新的词都检测一下逆序是不是存在, 不存在
#的话把这个词加入hash, 存在的话就输出

import sys

file = '1.txt'

if  len(sys.argv)>1:
	file = sys.argv[1]

f=open(file,'r')
lines=f.readlines()
f.close()

hash={}
for line in lines:
	line=line.replace('\n','')
	if hash.has_key(line[::-1]):
		print line
	else:
		hash[line]=1

print '--------hash_tbl:'
for i in hash:
	print i