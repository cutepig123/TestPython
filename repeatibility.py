import os, sys


	
def	ReadPlayList(path):
	cont=""
	for mPath in os.listdir(path):
		fullPath=os.path.join(path,mPath)
		result_xml = os.path.join(path,mPath+"\\result.xml")
		if os.path.isdir(fullPath) and os.path.isfile(result_xml):
			cont = cont + '<logcase>' + fullPath + '</logcase>\n'
	return cont
	
def GenGeneralInfoFile(path, GeneralInfo_xml_path):
	playlist = ReadPlayList(path)

	current_fdr = 'J:\\App\\User\\aeejshe\\Python25_2\\'
	cont = open(current_fdr + '\\GeneralInfo_template.xml','r').read()
	cont = cont.replace('$logcase$',playlist)
	
	fpw = open(GeneralInfo_xml_path,'w')
	fpw.write(cont)
	fpw.close()	

def GenReport(path, GeneralInfo_xml_path):
	cmd = 'C:\\wineagle\\system\\Report\\RepeatabilityReport\\Repeatability.exe %s %s abc'%(GeneralInfo_xml_path, path)
	print cmd
	os.system(cmd)

path = sys.argv[1]
GeneralInfo_xml_path = path + '\\GeneralInfo.xml'
GenGeneralInfoFile(path,GeneralInfo_xml_path)
GenReport(path,GeneralInfo_xml_path)
