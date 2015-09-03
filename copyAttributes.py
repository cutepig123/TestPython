'''

- Copy attribute.txt under one folder to all subfolders (starts with WIS) under another folder

'''

import os,sys
import ConfigParser,pdb,math,string
import time ,pdb

nCases=0
g_Alwaysoverwrite=0

def MySystem(cmd):
	global nCases
	print nCases, cmd
	nCases =nCases+1
	os.system(cmd)

def getvalue(file, str):
	for line in open(file,'r').readlines():
		p =line.find(str)
		if p>=0:
			return line[(p+len(str)):].strip()
			
def replacefunction(file, new_str):
	print '%s: replace function to-> %s'%(file, new_str)
	MySystem('copy /y "%s" "%s"'%(file, '%s.1'%file))
	isFunctionSec =0
	isWritten=0
	fpw =open(file,'w')
	for line in open('%s.1'%file,'r').readlines():
		#srch [Function]
		line =line.strip()
		if len(line)>=2 and line[0]=='[' and line[-1]==']':
			if( 'Function' in line ):
				isFunctionSec=1
			else:
				isFunctionSec=0
			fpw.writelines([line,'\n'])
		else:
			if isFunctionSec:
				if not isWritten:
					fpw.writelines([new_str,'\n\n'])
					isWritten=1
			else:
				fpw.writelines([line,'\n'])
	fpw.close()
	
MsgMap=[]

#############################
#For Message Type
StartInspect= 1
CreateAndSaveRecord = 2
SetCalibrationRecord = 4
Calib = 16

AutoLighting = 41
SimpleGeneral = 46
GetBeltVibData = 47
GetBeltVibDataWoWafer = 49

######################
#for calib
Calib2D = 3
Calib3D_Grab1 = 4
Calib3D_Grab2 = 5
Calib3D_Grab3 = 6
Calib3D = 7
CalibZ = 8

#######################
#for SimpleGeneral
UpdateZBegin = 11
UpdateZInsp0Deg = 12
UpdateZInsp90Deg = 13
UpdateZEnd = 14
UpdateZInsp180Deg = 15
	
MsgMap.append( [StartInspect, 'Thickness\nPartition thickness\nTTV\nWarp\nBow\nSaw mark\nRoughness\n'] )
MsgMap.append( [CreateAndSaveRecord, 'Learn'] )
MsgMap.append( [SetCalibrationRecord, 'Z calib'] )
MsgMap.append( [AutoLighting, 'AutoLighting'] )
MsgMap.append( [GetBeltVibData, 'Vib checking with wafer'] )
MsgMap.append( [GetBeltVibDataWoWafer, 'Vib checking without wafer'] )
MsgMap.append( [Calib, Calib2D, '2D calib'] )
MsgMap.append( [Calib, Calib3D_Grab1, '3D calib'] )
MsgMap.append( [Calib, Calib3D_Grab2, '3D calib'] )
MsgMap.append( [Calib, Calib3D_Grab3, '3D calib'] )
MsgMap.append( [Calib, Calib3D, '3D calib'] )
MsgMap.append( [Calib, CalibZ, 'Z calib'] )
MsgMap.append( [SimpleGeneral, UpdateZBegin, '0-90deg calib'] )
MsgMap.append( [SimpleGeneral, UpdateZInsp0Deg, '0-90deg calib'] )
MsgMap.append( [SimpleGeneral, UpdateZInsp90Deg, '0-90deg calib'] )
MsgMap.append( [SimpleGeneral, UpdateZEnd, '0-90deg calib'] )
	
def UpdateAttributeFile(folder):
	global MsgMap
	file ='%s\\cmdrpy.log'%folder
	msg_typ =getvalue(file, 'Message Type =')
	msg_type=int(msg_typ)
	m_type=(getvalue(file, 'm_type ='))
	if m_type is not None:
		m_type=int(m_type)
	
	isFind=0
	for msg in MsgMap:
		if (len(msg)==2 and msg[0]==msg_type) or (len(msg)==3 and msg[0]==msg_type and msg[1]==m_type):
			#pdb.set_trace()
			replacefunction('%s\\attribute.txt'%folder, msg[-1])
			isFind=1
			break
	if not isFind:
		print 'Cannot find msg_type', msg_type,'m_type',m_type,'in',MsgMap
		#pdb.set_trace()
	
def MyCopy(src_file, dest_fdr):
	global nCases
	#global g_Alwaysoverwrite
	print '--',dest_fdr,dest_fdr.lower().split('\\')[-1]
	if dest_fdr.lower().split('\\')[-1].startswith('wis'):
		dest_file ='%s\\attribute.txt'%dest_fdr
		#pdb.set_trace()
		#if g_Alwaysoverwrite:
		MySystem('copy /y "%s" "%s"'%(src_file, dest_fdr))
		UpdateAttributeFile(dest_fdr)
	else:
		#print 'Not WIS:', dest_fdr.lower().split('\\')[-1]
		for f in os.listdir(dest_fdr):
			f_full ='%s\\%s'%(dest_fdr,f)
			if os.path.isdir(f_full):
				MyCopy( src_file, f_full)
			
MyCopy(sys.argv[1]+'\\attribute.txt',sys.argv[2])
