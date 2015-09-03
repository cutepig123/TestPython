from pprint import pprint
import os,sys

def extractTime(line, str):
	s= str
	p1= line.find(s)
	if p1>=0:
		return float( line[ (p1+len(s)) :] )
	return None
	
def mypprint	(m):
	ks =m.keys()
	ks.sort()
	for k in ks:
		print k,'\t', m[k],'\t',
	print 
def extractTimeDiff(file):
	ts={}
	subss=['Begin SPI Insp,', 'End SPI Insp,','Fine 3D Construct begin,','Fine 3D Construct end,','Before VMTWrapper_SubmitJob(),','After VMTWrapper_SubmitJob(),']
	for line in open(file,'r').readlines():
		for subs in subss:
			tbegins =extractTime(line, subs)
			if tbegins is not None:
				ts[subs] =tbegins
	
	assert(len(ts)==len(subss))
	
	ts2={}
	tbegin=ts['Begin SPI Insp,']
	for k in ts.keys():
		ts2[  ts[k] -tbegin ] = k
	return ts2
	
RootFdr=r'C:\wineagle\log\AutoRpt_1'
RootFdr=r'\\Vis_led_insp04\c\wineagle\log\AutoRpt'
for fdrname in os.listdir(RootFdr):
	fpath = '%s\\%s\\TimeLog(MainThread).csv'%(RootFdr,fdrname)
	if os.path.isfile(fpath):
		print fpath,
		mypprint( extractTimeDiff(fpath) )
		