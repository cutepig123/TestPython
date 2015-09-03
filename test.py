import os,sys

BatchPath=r'G:\AutoTest\TestScheme'
os.system(r'set path=c:\WinEagle;c:\wineagle\lib;c:\Wineagle\asmhmi;C:\WinEagle\Utilities\Tools\General;%path%')

envList={'ASM_VIS_LOG_DATA':r'c:\WinEagle\Log',
		'ASM_VIS_LOG_AUTOREPEAT':r'c:\WinEagle\log\AutoRpt',
		'PopReport':1,
		'IsRunLastGood':0,
		'RunOnceFlag':0,
		}

for envStr in envList:
	if os.getenv(envStr) == None:
		os.putenv(envStr,str(envList[envStr]) )
	envList[envStr]=os.getenv(envStr)
for envStr in envList:
	print envStr,envList[envStr]
	
WinLogPath = envList['ASM_VIS_LOG_DATA']
AutoRptLogPath =envList['ASM_VIS_LOG_AUTOREPEAT']
PopReport = envList['PopReport']
IsRunLastGood = envList['IsRunLastGood']
RunOnceFlag=envList['RunOnceFlag']

#print '* Please Enter the path of your TestSuite.txt '
PathPLPL = r'G:\AutoTest\TestScheme\SmokeTest'
if RunOnceFlag:
	pass