import ConfigParser,pdb

class MyCfg:
	def __init__(self):
		self._cfg =ConfigParser.ConfigParser()
	def read(self, f):
		return self._cfg.read(f)
	def get(self,section,field):
		#srch section
		# secIdx=-1
		# isFind =0
		# for sec in self._cfg.sections():
			# if sec.lower()==section.lower():
				# isFind =1
				# break
			# secIdx =secIdx+1
		# if not isFind:
			# return None
		
		try:
			for item in self._cfg.items(section.lower()):
				assert(len(item)==2)
				if item[0].lower()==field.lower():
					return item[1]
		except:
			return None
			
cfg =MyCfg()
cfg.read('SysAttribute.txt')
print cfg.get('General','Optics0')
pdb.set_trace()
