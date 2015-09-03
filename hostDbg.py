import os,sys,re

#only support folder with name "WISIxxx"
path=r'c:\wineagle\log\hostdbg.txt'
if len(sys.argv)>1:
	path=sys.argv[1]

fp1=open('m_SetWafIDInfos.txt','w')
fp2=open('m_InspDoneInfos.txt','w')
fp3=open('m_EventDoneInfos.txt','w')
for line in open(path,'r').readlines():
	#m_SetWafIDInfos
	if re.search('^[0-9]+ [0-9]+ ',line) and len(line.split())==5 is not None:
		fp1.writelines([line])
	elif re.search('^[0-9]+ [0-9]+ ',line) and len(line.split())==7 is not None:
		fp3.writelines([line])
	elif re.search('^[0-9]+ ulWafID ',line)  is not None:
		fp2.writelines([line])
fp1.close()		
fp2.close()
fp3.close()

