import os,sys,ConfigParser 

def	findString(str,lis):
	currSec=None
	for sec in lis:
		if sec.strip().lower()== str.lower():
			currSec = sec
			break
	return currSec

def findKeyValue(str,lis):	
	currSec=None
	currValue=None
	for sec in lis:
		if sec[0].strip().lower()== str.lower():
			currSec = sec
			currValue = sec[1]
			break
	return currValue
	
def	findKeyValue2(conf_reader,section,key,value_default):
	value=value_default

def	ImageList(path):
	lis=[]
	for root, dirs, files in os.walk(path, topdown=False):	
		for name in files:	
			#os.remove(os.path.join(root, name))	
			fileName=os.path.join(root, name)
			if name.lower().endswith('.bmp') and name.lower().startswith('buffer'):
				#print fileName
				lis.append(fileName)
	
	return lis;

def	setApplcn(learn_path, station_id, record_id, criteria_id):
	#modify appconrt.txt
	if not os.path.isdir(learn_path):
		print learn_path,"Not exist!"
		assert(0)
		
	appcon_path=learn_path+"\\appconrt.txt"
	conf_reader = ConfigParser.ConfigParser()
	conf_reader.read(appcon_path)
	#record_value= conf_reader.get("station%d" %(station_id), "RECORD ID".lower(),"")
	#print 'record_value',record_value
	#crit_value= conf_reader.get("station%d" %(station_id), "CRITERIA ID".lower(),"")
	#print 'crit_value',crit_value
	conf_reader.set("station%d" %(station_id), "RECORD ID".lower(),record_id)
	conf_reader.set("station%d" %(station_id), "CRITERIA ID".lower(),criteria_id)
	conf_reader.write(open(appcon_path,'w'))
	#print "OK"
	
	
def	setImage(learn_path):
	#modify appconrt.txt
	if not os.path.isdir(learn_path):
		print learn_path,"Not exist!"
		assert(0)
		
	#modify images.txt
	lis = ImageList(learn_path+"\\record")
	print "find", len(lis), "images"
	for i in range(len(lis)):
		print i, lis[i][-60::]
	
	ID=raw_input('input image ID:[0]')
	if len(ID)==0: 
		ID = 0
	else:
		ID=int(ID)
	
	fp=open(learn_path+"\\images.txt","w")	
	fp.write(lis[ID])
	fp.close
	
	
learn_path = raw_input('input learn path:[C:\\WinEagle]')
if len(learn_path)==0:
	learn_path = "C:\\WinEagle"
	
station_id = raw_input('input station id[]')
if len(station_id)>0:
	record_id = raw_input('input record id')
	criteria_id = raw_input('input criteria id')
	setApplcn(learn_path,int(station_id),int(record_id),int(criteria_id))
setImage(learn_path)

