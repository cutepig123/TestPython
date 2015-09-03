import os,sys

file=r'\\ahkex\ahkproj\Vision\app\Public\APPLTEST\AppAutoTestScheme\DailyBuildLog\LabelCheck\Log.txt'
fp=open(file,'r')

stage_basefile =0
stage_curfile =1
stage_ver =2

stage=stage_basefile

file_base=''
file_curr=''
file_rev=''
for line in fp.readlines():
	line =line.strip()
	if len(line)==0:
		continue
	if stage==stage_basefile:
		file_base =line
		stage=stage_curfile
	elif stage==stage_curfile:
		file_curr =line
		stage=stage_ver
	elif stage==stage_ver:
		file_rev =line
		p1=file_rev.find('ArchiveRevision:Labels=[')
		assert(p1==0)
		n1=len('ArchiveRevision:Labels=[')
		revs =file_rev[n1:-1]
		pL =revs.find('Latest Version')
		stage=stage_ver
	