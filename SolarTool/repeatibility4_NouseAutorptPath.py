import os, sys

#gen reports from a folder
	
class Case:
	def __init__(self):
		#self.report_name=""
		self.autorptpath=""
		self.path=""
	def prints(self):
		print self.autorptpath, self.path
		
#return 	[PlayList]
def	genCasesCont(Cases):	
	cont=""
	
	for case in Cases:
		cont = cont + '<logcase>' + case.path + '</logcase>\n'
			
	return cont
	
def GenGeneralInfoFile(playList_cont, GeneralInfo_xml_path):
	current_fdr = 'J:\\App\\User\\aeejshe\\Python25_2\\'
	cont = open(current_fdr + '\\GeneralInfo_template.xml','r').read()
	cont = cont.replace('$logcase$',playList_cont)
	
	fpw = open(GeneralInfo_xml_path,'w')
	fpw.write(cont)
	fpw.close()	

def GenReport(path, GeneralInfo_xml_path, report_name):
	cmd = 'C:\\wineagle\\system\\Report\\RepeatabilityReport\\Repeatability.exe %s %s %s'%(GeneralInfo_xml_path, path,report_name)
	print cmd
	os.system('echo copy /y %s.xml generalinfo.xml  >%s\\%s.bat'%( report_name, path, report_name) )
	os.system('echo %s >>%s\\%s.bat'%( cmd, path, report_name) )
	os.system(cmd)

def getValue(line):
	s='<ptyVal>'
	p1 = line.find(s)
	assert(p1>0)
	p1 = p1+len(s)
	
	s='</ptyVal>'
	p2 = line.find(s,p1)
	assert(p2>0)
	
	value = line[p1:p2]
	
	#print value,
	#value = float(value)
	return value
	
def findAutoRptPath( input_file_resultxml ):
	fp=open(input_file_resultxml,'r')
		
	#read contents
	conts = ''.join(fp.readlines())
	p1=0
	
	#AutoRpt Path
	AutoRpt_Path="N.A."
	s='<pty name="AutoRpt Path">'
	p1=conts.find(s,p1)
	if (p1>0):
		AutoRpt_Path = getValue(conts[p1:])
	
	fp.close()
	
	return AutoRpt_Path
	
#return {string, [Case]}		
def processAll2(top, output):
	
	
	for dir in os.listdir(top):
		dirName=os.path.join(top, dir)
		if not os.path.isdir(dirName):
			continue
		if dir.startswith('WIS'):
			#if find a case folder,then add to the output
			fileName=os.path.join(dirName, 'result.xml')
			if not os.path.isfile(fileName):
				continue
			print fileName,
			AutoRpt_Path = findAutoRptPath( fileName )
			print AutoRpt_Path,
			case = Case()
			case.autorptpath = AutoRpt_Path 
			case.path = dirName
			
			#key1 = '.'.join(AutoRpt_Path.split('\\')[1:-1]) + '.'.join(AutoRpt_Path.split('\\')[-1].split('.')[1:])
			key2 = '.'.join(dirName.split('\\')[1:-1]) + '.'.join(dirName.split('\\')[-1].split('.')[1:])
			#key = '%sXX%s'%(key1,key2)
			key =key2
			
			key = key.replace(' ','').replace('\t','')
			#key = (AutoRpt_Path.split('\\')[2]) +'.'.join(AutoRpt_Path.split('\\')[-1].split('.')[1:-1])
			print key
			if output.has_key(key):
				output[key].append(case)
			else:
				output[key]=[case]
		else:
			processAll2(dirName, output)

def DelOldReport(top):
	for dir in os.listdir(top):
		dirName=os.path.join(top, dir)
		if not os.path.isdir(dirName):
			continue
		if dir.endswith('_files'):	#need delete
			cmd='rmdir /s/q "%s"'%dirName
			print cmd
			os.system(cmd)
		else:
			DelOldReport(dirName)
			
def CreateEmptyFile(file,  cols):
	fpw=open(file,'w')
	data = cols.replace(',','<td>')
	head = '<table name="summary" border="1"><tr>'+ data +'</tr>\n'
	fpw.writelines([ head])
	fpw.close()
	
def mains(path):	#path of folder
	os.system(r'copy/y j:\app\User\aeejshe\Python25_2\Solar3D_INSP.xml c:\wineagle\System\Report\Module\Solar3D_INSP.xml')
	path_autorpt = path
	GeneralInfo_xml_path = path_autorpt + '\\GeneralInfo.xml'
	conts = {}
	DelOldReport(path)
	processAll2(path, conts)
	print 'num playlist:', len(conts)
	#print conts
	#os.system('pause')
	for key in conts.keys():
		cases = conts[key]	#[case]
		print key
		if len(cases)<2: continue
		report_name = key
		cont=genCasesCont(cases)
		print "processing:", report_name
		
		for case in cases: case.prints()
		
		print "\tGenGeneralInfoFile"
		GenGeneralInfoFile(cont,GeneralInfo_xml_path)
		
		print "\tGenReport"
		GenReport(path_autorpt, GeneralInfo_xml_path, report_name)
		
		print "\trename GeneralInfo"
		newGeneralInfo_xml_path = "%s\\%s.xml" %(path_autorpt , report_name)
		cmd="copy /y %s %s"%(GeneralInfo_xml_path, newGeneralInfo_xml_path)
		print '\t',cmd
		os.system( cmd )
		
		#os.system("pause")
		

path = sys.argv[1]
mains(path)