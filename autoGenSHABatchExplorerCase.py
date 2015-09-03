import os,sys

shalog=r'E:\Solar\case\20150523\mydir_shas001.ept.dec\gsd001.log'
id=0
prefix=r'E:\Solar\case\20150523\Cam%dFullImageExp0.10_'%id
N=7710
file_des =r'E:\Solar\case\20150523\mydir_shas001.ept.dec\%d.txt'%id

fp =open(file_des,'w')
for i in range(N):
	fp.write('%s\t%s%d.bmp\n'%(shalog,prefix,i))
fp.close()
	