import os,sys

class MyMap:
	def __init__(self):
		self.d =[]
	def Set(self,k,v):
		for x in self.d:
			if x[0]==k:
				x[1]=v
				return
		self.d.append([k,v])
	def Get(self,k):
		for x in self.d:
			if x[0]==k:
				return x[1]
		return None
	def GetAll(self):	
		return self.d
		
class Cfg:
	def __init__(self):
		self.secs=MyMap()
	def Set(self, sec, key, val):
		v= self.secs.Get(sec)
		if v is None:
			v=MyMap()
			v.Set(key, val)
			self.secs.Set(sec,v)
			return
		v.Set(key,val)
	def ToXml(self):	
		print '<%s>\n'%'ROOT'
		secs= self.secs.GetAll()
		
		#CMD
		sec =secs[0]
		print '<%s>\n'%sec[0]
		for fld in sec[1].GetAll():
			print '<%s>%s</%s>\n'%(fld[0],fld[1],fld[0])
		print '</%s>\n'%sec[0]
		
		#RPY
		print '<%s>\n'%'RPY'
		for sec in secs[1:]:
			print '<%s>\n'%sec[0]
			for fld in sec[1].GetAll():
				print '<%s>%s</%s>\n'%(fld[0],fld[1],fld[0])
			print '</%s>\n'%sec[0]
		print '</%s>\n'%'RPY'
		
		#END
		print '</%s>\n'%'ROOT'

def GenXml(cmd_rpy_path):
	Sec=''
	field=[]
	cfg=Cfg()
	for line in open(cmd_rpy_path,'r').readlines():
		
		p =line.find('#')
		if p>=0: 
			line =line[:p]
		line =line.strip()
		if len(line)==0:
			continue
		if line.startswith('[') and line.endswith(']'):
			Sec =line[1:-1].strip()
			continue
		fld =line.split('=')
		if len(fld)==2:
			field=[x.strip() for x in fld]
			field[0] =field[0].replace(' ','_')
			#print field
			cfg.Set(Sec,field[0],field[1])
			continue
	cfg.ToXml()

GenXml(sys.argv[1])
