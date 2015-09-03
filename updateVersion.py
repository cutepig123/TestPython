import os,sys,subprocess

file =r'G:\Itf\Include\VERSION.H'

def getCurrentGitVersion():
	os.chdir('g:\\')
	os.environ['path']='C:\\Program Files\\Git\\bin;C:\\Program Files (x86)\\Git\\bin;' +os.environ['path']
	#value = subprocess.call('echo %path%', shell=True)
	#print value
	#return subprocess.call('git rev-parse HEAD', shell=False)
	return os.popen('git rev-parse HEAD').read()
	
#define ITF_PR_VERSION_NO                "3.553T07 "	 /* Version number */
fp=open(file,'r')
Cont=fp.readlines()
fp.close()

for i in range(len(Cont)):
	#print line
	line =Cont[i]
	if line.find('ITF_PR_VERSION_NO')>=0:
		p1=line.find('"')
		assert(p1>=0)
		p2=line.find('"',p1+1)
		assert(p2>=0)
		version =line[(p1+1):p2].strip()
		print version
		
		git_ver= getCurrentGitVersion().strip()
		print git_ver
		
		if len(version) > len(git_ver):
			version =version[0:(len(version) - len(git_ver)-1)]
		version =version +'_'+git_ver
		print version
		
		Cont[i] ='#define ITF_PR_VERSION_NO \"%s\"'%(version)
		break
#print Cont		

fp=open(file,'w')
fp.writelines(Cont)
fp.close()
