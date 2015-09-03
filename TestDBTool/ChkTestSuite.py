import os,sys

folder=sys.argv[1]

def chk_playlist(folder):
	playlist ='%s\\playlist.txt'%folder
	assert os.path.isfile(playlist), playlist
	
	cases_add={}
	cases_add['calo0002']=0
	cases_add['calo0005']=0
	
	lines =os.open(playlist,'r').readlines()
	for line in lines:
		line =line.strip()
		if len(line)==0 or line[0]=='#':
			continue
		assert os.path.isdir(line),line
		assert line.lower().startswith(folder.lower()), '%s not in %s'%(line,folder)
		short_case =line.lower().split('\\')[-1] 
		if short_case in cases_add.keys():
			cases_add[short_case]=1
	is_modified=0
	for k in short_case.keys():
		if short_case[k]==0:
			lines =
		
for line in open(folder+"\\testsuite.txt","r").readlines():
	line =line.strip()
	if len(line)==0 or line[0]=='#':
		continue
	assert os.path.isdir(line), line
	
	chk_playlist(line)
	