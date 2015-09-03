'''

'''

import os,sys
import ConfigParser,pdb,math,string
import time 
import copy

logIntermed =1

def LogError(s):
	global fpErrLog
	print >>fpErrLog, s
	
class MyMap:
	def __init__(self):
		self.data=[]
	def keys(self):
		k=[]
		for i in self.data:
			assert(len(i)==2)
			k.append(i[0])
		return k
	def __len__	(self):
		return len(self.data)
		
	def set(self,key,val):
		for i in self.data:
			assert(len(i)==2)
			if i[0]==key:
				i[1]=val
				return
		self.data.append([key,val])
	def get(self,key):
		for i in self.data:
			assert(len(i)==2)
			if i[0]==key:
				return i[1]
		return None
		
	def empty(self):
		return len(self.data)==0
	
	def __repr__(self):
		s=self.data.__repr__()
		return s
		
class AttrLoader:
	def __init__(self, f, isReadSysCfg):
		#for check only
		self.optics=[]
		self.pkgs=[]
		
		#global..
		self.ftns=[]
		self.condn=[]
		
		self.dev=[]
		
		#combinations, for sys attribute
		self.combOpticsPkgFtns=MyMap()
		self.combOpticsPkgDevs=MyMap()
		self.combOpticsConds=MyMap()
		
		cur_section=''
		is_global_function_readed =0
		for line in open(f,'r').readlines():
			line =line.strip().lower()	# all are lower case
			#print line
			#pdb.set_trace()
			
			if len(line)==0 or line[0]=='#':
				continue
			if line[0]=='[':	#section
				if not( line[-1]==']'):
					raise Exception('File: %s, Invalid section format: %s'%(f,line))
				cur_section =line[1:-1]
				cur_section =cur_section.strip()
			else:			#field
				if not( len(cur_section)>0 ):
					raise Exception('File: %s, Field %s found before any section'%(f,line))
				if cur_section=='optics':
					self.optics.append(line)
				elif cur_section=='PackageType'.lower():
					self.pkgs.append(line)
				elif cur_section=='Function'.lower():
					self.ftns.append(line)
					is_global_function_readed=1
				elif cur_section=='Condition'.lower():
					self.condn.append(line)
				else: 
					if isReadSysCfg:
						# check current section format
						# the section must be x.x.device or x.x.function format!
						x =cur_section.split('.')
						if not(len(x)==3):
							raise Exception('File: %s, section name %s should have 3 parts!'%(f,cur_section))
						if not(x[0] in self.optics):
							raise Exception('File: %s, line %s, %s does not exists in optics list!'%(f,line,x[0]))
						if not(x[1] in self.pkgs):
							raise Exception('File: %s, line %s, %s does not exists in package type list!'%(f,line,x[1]))
						
						if(x[-1]=='device'):	#update combOpticsPkgDevs
							key ='%s$%s'%(x[0],x[1])
							dev =self.combOpticsPkgDevs.get(key)
							if dev is None:
								dev=MyMap()
							dev.set(line, 0)
							self.combOpticsPkgDevs.set(key, dev)
							
							if not(is_global_function_readed):
								raise Exception('File: %s, line %s, function should defined before device!'%(f,line))
							
							#update combOpticsPkgFtns
							#Remarks: [function] MUST before all [device]
							for ftn in self.ftns:
								key ='%s$%s$%s'%(x[0],x[1],ftn)
								self.combOpticsPkgFtns.set(key,0)
								
							self.dev.append(line)
							
						elif(x[-1]=='function'):	#update combOpticsPkgFtns
							key ='%s$%s$%s'%(x[0],x[1],line)
							self.combOpticsPkgFtns.set(key,0)
							
							#Remarks: [xxx.device] MUST defined before [xx.function]!
							key ='%s$%s'%(x[0],x[1])
							if not( key in self.combOpticsPkgDevs.keys() ):
								raise Exception('File: %s, line %s, %s does not exists!'%(f,line,key))
						else:
							raise Exception('File: %s, line %s, invalid section format!'%(f,line))
					else:
						if cur_section=='device'.lower():
							self.dev.append(line)
						else:
							raise Exception('File: %s, line %s, invalid section name %s!'%(f,line,cur_section))

		if not isReadSysCfg:
			if not( len(self.optics)==1 ):
				raise Exception('File: %s, line %s, optics number must be 1!'%(f,line))
			if not( len(self.pkgs)==1 ):
				raise Exception('File: %s, line %s, pcakage number must be 1!'%(f,line))
			if not( len(self.dev)==1 ):
				raise Exception('File: %s, line %s, device number must be 1!'%(f,line))
			if not( len(self.condn)>=1 ):
				raise Exception('File: %s, line %s, condition number >=1!'%(f,line))
			if not( len(self.ftns)>=1 ):
				raise Exception('File: %s, line %s, function number >=1!'%(f,line))
			
			#update combOpticsPkgDevs
			dev=MyMap()
			dev.set(self.dev[0], 0)
			key ='%s$%s'%(self.optics[0],self.pkgs[0])
			self.combOpticsPkgDevs.set(key, dev)
			
			for ftn in self.ftns:
				key ='%s$%s$%s'%(self.optics[0],self.pkgs[0],ftn)
				self.combOpticsPkgFtns.set(key,0)
			
		#update combOpticsConds
		for optics in self.optics:
			for cond in self.condn:
				key ='%s$%s'%(optics,cond)
				self.combOpticsConds.set(key,0)
	
	def __str__(self):
		s = 'Optics:'
		s = s +('\t'.join(self.optics) + '\n')
		s = s +('Packages:')
		s = s +('\t'.join(self.pkgs) + '\n')
		s = s +('Devices:')
		s = s +('\t'.join(self.dev) + '\n')
		s = s +('Conditions:')
		s = s +('\t'.join(self.condn) + '\n')
		s = s +('Functions:')
		s = s +('\t'.join(self.ftns) + '\n')
		s = s +'combOpticsPkgFtns:'
		s = s +'%s\n'%self.combOpticsPkgFtns
		s = s +'combOpticsPkgDevs:'
		s = s +'%s\n'%self.combOpticsPkgDevs
		s = s +'combOpticsConds:'
		s = s +'%s\n'%self.combOpticsConds
		
		return s	
	
class SysAttr:
	def __init__(self, f):
		self.sysAttr =AttrLoader(f, 1)
		self.casepath=f
		self.NCase=0
	
	def __update(self,I, O):
		N=0		
		for key in I.keys():
			v =O.get(key)
			if v is None:
				LogError('File: %s, key %s does not exist!'%(self.casepath, key))
				continue
			O.set(key,v+1)
			N =N+1
		if(N==0):
			LogError('File: %s, No valid attribute found!'%(self.casepath))
		return N
		
	def __updateDevs(self,I, O):
		N=0	
		for keyI in I.keys():
			vI =I.get(keyI)
			vO =O.get(keyI)
			if vO is None:
				LogError('File: %s, key %s does not exist!'%(self.casepath, keyI))
				continue
			for vIkey in vI.keys():
				vvO =vO.get(vIkey)
				if vvO is None:
					LogError('File: %s, key %s does not exist!'%(self.casepath, vIkey))
					continue
				vO.set(vIkey,vvO+1)
				N =N+1
		if(N==0):
			LogError('File: %s, No valid attribute (for dev) found!'%(self.casepath))
		return N
	
	def __getScore(self,I):
		#s= '%s'%I
		
		N=len(I.keys())
		S=0.0
		for i in I.keys():
			v =I.get(i)
			assert(v>=0)
			if v>0:
				S =S+1.0
		#s = s+ '\nScore: %f'%(S/N)
		return S/(0.001+N)
		
	def __getScoreDevs(self,I):
		#pdb.set_trace()
		#s= '%s'%I
		
		N=len(I.keys())
		S=0.0
		for i in I.keys():
			v =I.get(i)
			#v is a map
			x=0
			for k in v.keys():
				#x is device name
				nCase =v.get(k)
				#nCase is number  cases for the dev
				assert( nCase>=0)
				if nCase>0:
					x =x+1
			#pdb.set_trace()
			S = S+min(x,0.5)+0.5*(1-math.exp(-0.2*x))
		#s = s+ '\nScore: %f'%(S/N)
		return S/(0.001+N)
		
	def readCase(self,fil,fpLog):
		global logIntermed
		#pdb.set_trace()
		myAttr =AttrLoader(fil, 0)
		if(logIntermed):
			print >>fpLog,myAttr
			
		for i in myAttr.optics:
			if not( i in self.sysAttr.optics ):
				raise Exception('File: %s, optics %s does not exist!'%(fil,i))
			
		for i in myAttr.pkgs:
			if not( i in self.sysAttr.pkgs ):
				raise Exception('File: %s, package %s does not exist!'%(fil,i))
			
		for i in myAttr.dev:
			if(not i in self.sysAttr.dev ):
				raise Exception('File: %s, device %s does not exist!'%(fil,i))
			
		for i in myAttr.condn:
			if not( i in self.sysAttr.condn ):
				raise Exception('File: %s, condition %s does not exist!'%(fil,i))
		
		#for i in myAttr.ftns:
		#	if not( i in self.sysAttr.ftns ):
		#		raise Exception('File: %s, function %s does not exist!'%(fil,i))
			
		N =self.__update( myAttr.combOpticsPkgFtns, self.sysAttr.combOpticsPkgFtns)
		M =	self.__updateDevs( myAttr.combOpticsPkgDevs, self.sysAttr.combOpticsPkgDevs)
		K =self.__update( myAttr.combOpticsConds, self.sysAttr.combOpticsConds)
		
		self.NCase =self.NCase+1
		return [N,M,K]
	
	def getAllScore(self):
		Cf =S1 =self.__getScore(self.sysAttr.combOpticsPkgFtns)
		Cp =S2 =self.__getScoreDevs(self.sysAttr.combOpticsPkgDevs)
		Cc =S3 =self.__getScore(self.sysAttr.combOpticsConds)
		S =(S1*S2*S3)
		return [Cf,Cp,Cc,S]
		
	def __str__(self):
		s='NCase: %s\n'%(self.NCase)
		s= s+'Function coverage:\n'
		S1 =self.__getScore(self.sysAttr.combOpticsPkgFtns)
		s= s+'%s\nScore:'%self.sysAttr.combOpticsPkgFtns+'%f'%S1
		s= s+'\nDevice coverage:\n'
		S2 =self.__getScoreDevs(self.sysAttr.combOpticsPkgDevs)
		s= s+'%s\nScore:'%self.sysAttr.combOpticsPkgDevs+'%f'%S2
		s= s+'\nCondition coverage:\n'
		S3 =self.__getScore(self.sysAttr.combOpticsConds)
		s= s+'%s\nScore:'%self.sysAttr.combOpticsConds+'%f\n'%S3
		S =(S1*S2*S3)
		s= s+'Total score:%f\n'%S
		
		return s
		


def WriteExcel(file, sheetName, score,Cf,Cp,Cc,NCase):
	from win32com.client import Dispatch
	xlApp = Dispatch("Excel.Application") 
	xlApp.Visible = 1
	
	
	xlApp.Workbooks.Open(file)
	
	if not(xlApp.Workbooks.Count>0):
		raise Exception('File: %s, no work books!'%(file))
	workbook = xlApp.Workbooks[0]
	
	ThisSheet=None
	#TemplateSheet=None
	for i in range( workbook.Sheets.Count ):
		# If yes, use the first sheet of current workbook.
		sheet = workbook.Sheets[i]
		if (sheet.name.lower()==sheetName.lower()):
			ThisSheet =sheet
			break
		#if (sheet.name.lower()=='template'):
		#	TemplateSheet =sheet
			
	if ThisSheet is None:
		#assert(TemplateSheet is not None)
		#ThisSheet = TemplateSheet.Copy()
		ThisSheet =workbook.Sheets['Template'].Copy()
		#bugs here!
		raise Exception('File: %s, no work sheet %s!'%(file,sheetName))
		#pdb.set_trace()
		ThisSheet.name =sheetName
		
	today  = time.strftime("%Y_%m_%d", time.localtime())
	print 'today is ',today
	
	for y in xrange(2, 1000):
		# Cells( <row>, <column>)
		
		v =ThisSheet.Cells(y,1).Value
		print v
		#pdb.set_trace()
		if( v is None or len('%s'%v)==0 ):
			print 'update row', y, 'to', today, score
			ThisSheet.Cells(y,1).Value =today
			ThisSheet.Cells(y,2).Value =score
			ThisSheet.Cells(y,3).Value =Cf
			ThisSheet.Cells(y,4).Value =Cp
			ThisSheet.Cells(y,5).Value =Cc
			ThisSheet.Cells(y,6).Value =NCase
			
			break
		if( today==v ):
			print 'update row', y, 'to', today, score
			ThisSheet.Cells(y,2).Value =score
			ThisSheet.Cells(y,3).Value =Cf
			ThisSheet.Cells(y,4).Value =Cp
			ThisSheet.Cells(y,5).Value =Cc
			ThisSheet.Cells(y,6).Value =NCase
			break
	
	workbook.Save()
		
#Main()
def handleOneTestSuite(path):
	global logIntermed
	
	testSuite =r'%s\TestSuite.txt'%path

	SysAttribute =r'%s\SysAttribute.txt'%path
	fnLog=r'%s\MyLog.txt'%path
	fpLog =open(fnLog,'w')
	
	sysAttr =SysAttr(SysAttribute)
		
	print 'Log file:',fnLog
	print >>fpLog, 'Load system setting..'
	print >>fpLog, sysAttr

	X =[]
	bMayReplace =0
	for line in open(testSuite,'r').readlines():
		line =line.strip().lower()
		if len(line)==0 or line[0]=='#':
			continue
		print >>fpLog, '===>',line
		print line
		
		# parse Z::::\\aaaex\aaaproj\VisionTesting like format
		X2 =line.split('<=>')
		if len(X2)>1:
			if not( len(X2)==2 ):
				LogError('File: %s, line %s, invalid format!'%(testSuite,line))
			bMayReplace=1
			X =X2
			X =[ x.strip().lower() for x in X]
			print X
			continue
		
		if (bMayReplace):
			line_ =line.replace(X[0],X[1])	
			if not line_==line:
				print '->', line_
				line =line_
				
		if(not os.path.isdir(line)):
			LogError('File: %s, line %s, is not folder!'%(testSuite,line))
		
		#read global settings
		if 0:
			f ='%s\\Attribute.txt'%line
			if (os.path.isfile(f)):
				try:
					n =sysAttr.readCase(f,fpLog)
					print >>fpLog,n, 'items updated!'
					if (logIntermed):
						print >>fpLog,sysAttr
				except Exception, e:
					LogError(e)
			else:
				LogError('File: %s, line %s, no Attribute.txt in the folder!'%(testSuite,line))
		
		playlist ='%s\\playlist.txt'%line
		if (os.path.isfile(playlist)):
			for line2 in open(playlist,'r').readlines():
				line2 =line2.strip().lower()
				if len(line2)==0 or line2[0]=='#':
					continue
				print >>fpLog, '==>',line2
				print line2
				
				if (bMayReplace):
					line2 =line2.replace(X[0],X[1])	
				if(not os.path.isdir(line2)):
					LogError('File: %s, line %s, case not exist!'%(playlist,line2))
				else:
					f ='%s\\Attribute.txt'%line2
					if (os.path.isfile(f)):
						try:
							n =sysAttr.readCase(f,fpLog)
							print >>fpLog,n, 'items updated!'
							if (logIntermed):
								print >>fpLog,sysAttr
						except Exception, e:
							LogError(e)
					else:
						LogError('File: %s, line %s, Attribute not exist!'%(playlist,line2))
		else:
			LogError('File: %s, not exist!'%(playlist))

	[Cf,Cp,Cc,S] =sysAttr.getAllScore()
	
	fpLog.close()
	
	return [Cf,Cp,Cc,S, sysAttr.NCase]
	
def Main(root):
	global logIntermed
	path='%s\\%s'%(root,'testsuite.txt')
	if  (os.path.isfile(path)):
		item=root.split('\\')[-1]
		[Cf,Cp,Cc,S, NCase]=handleOneTestSuite(root)
		xlspath ='%s\\score.xls'%root
		print 'S, Cf,Cp,Cc:',S, Cf,Cp,Cc
		WriteExcel(xlspath,item, S, Cf,Cp,Cc, NCase)
	else:		
		for f in os.listdir(root):
			path='%s\\%s'%(root,f)
			if not (os.path.isdir(path)):
				continue
			item=path.split('\\')[-1]
			print item
			#os.system('pause')
			[Cf,Cp,Cc,S,NCase]=handleOneTestSuite(path)
			xlspath ='%s\\score.xls'%root
			print 'S, Cf,Cp,Cc:',S, Cf,Cp,Cc
			WriteExcel(xlspath,item, S, Cf,Cp,Cc, NCase)
	
#root =r'\\vis_3d_pp\e$\JSHe\TestDB'	
root =sys.argv[1]
fpErrLog =open('%s\\Err.log'%(root),'w')
Main(root)
fpErrLog.close()
