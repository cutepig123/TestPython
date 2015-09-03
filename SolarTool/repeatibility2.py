import os, sys

#read config file casehit.txt, and gen data according to the config
	
class PlayList:
	def __init__(self):
		self.report_name=""
		self.cont=""	#playlists
		
#return 	[PlayList]
def	ReadPlayList(path):	#path of casehit.txt
	conts=[]
	
	case = None
	for line in open(path,"r").readlines():
		line = line.strip()
		if len(line)==0: continue
		
		if line.startswith("==>"):	#new report!
			if case is not None:	#only 1st time not called!
				conts.append(case)
				
			case = PlayList()
			case.report_name = line[3:].strip()
			print 'procesing',case.report_name
		else:
			fullPath = line.split(' -> ')[1].strip()
			result_xml = fullPath + '\\result.xml'
			print '\t',result_xml
			assert( os.path.isfile(result_xml) )
			case.cont = case.cont + '<logcase>' + fullPath + '</logcase>\n'
			
	return conts
	
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
	os.system(cmd)

	
def mains(path):	#path of casehit.txt
	path_autorpt = "c:\\wineagle\\log\\autorpt"
	GeneralInfo_xml_path = path_autorpt + '\\GeneralInfo.xml'
	conts = ReadPlayList(path)
	print 'num cases:', len(conts)
	#os.system('pause')
	for playlist in conts:
		print "processing:", playlist.report_name,
		
		print "\tGenGeneralInfoFile"
		GenGeneralInfoFile(playlist.cont,GeneralInfo_xml_path)
		
		print "\tGenReport"
		GenReport(path_autorpt, GeneralInfo_xml_path, playlist.report_name)
		
		print "\trename GeneralInfo",
		newGeneralInfo_xml_path = "%s\\%s.xml" %(path_autorpt , playlist.report_name)
		cmd="copy /y %s %s"%(GeneralInfo_xml_path, newGeneralInfo_xml_path)
		print '\t',cmd
		os.system( cmd )
		
		#os.system("pause")
		

path = sys.argv[1]
mains(path)