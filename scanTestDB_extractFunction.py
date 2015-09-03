'''

'''

import os,sys
import ConfigParser,pdb,math,string
import time 
import copy

logIntermed =1

def LogError(s):
	global fpErrLog
	print s
	print >>fpErrLog, s
	
def MySystem(s):
	global fpErrLog
	os.system( s)
	print s
	print >>fpErrLog, s	
	#os.system('pause')
	
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

def Main(root):
	global logIntermed
	
	for f in os.listdir(root):
		path='%s\\%s'%(root,f)
		if not (os.path.isdir(path)):
			continue
		FunctionRootPath ='%s\\Function_AutoSim'%path
		
		#create folder FunctionRootPath
		if os.path.isdir(FunctionRootPath):
			cmd='rd /s/q "%s"'%FunctionRootPath
			MySystem(cmd)
		if not os.path.isdir(FunctionRootPath):
			cmd='md "%s"'%FunctionRootPath
			MySystem(cmd)
		item=f
		testSuite =r'%s\TestSuite.txt'%path

		fnLog=r'%s\MyLog.txt'%path
		fpLog =open(fnLog,'w')

		X =[]
		bMayReplace =0
		for line in open(testSuite,'r').readlines():
			line =line.strip().lower()
			if len(line)==0 or line[0]=='#':
				continue
			print >>fpLog, '===>',line
			print line
			
			#pdb.set_trace()
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
			FunctionList=[]
			
			if not (os.path.isfile(playlist)):
				LogError('File: %s, not exist!'%(playlist))
				continue
			for line2 in open(playlist,'r').readlines():
				line2 =line2.strip().lower()
				if len(line2)==0 or line2[0]=='#':
					continue
				print >>fpLog, '==>',line2
				
				
				if (bMayReplace):
					line2 =line2.replace(X[0],X[1])	
				if(not os.path.isdir(line2)):
					LogError('File: %s, line %s, case not exist!'%(playlist,line2))
					continue
				
				f ='%s\\Attribute.txt'%line2
				if not (os.path.isfile(f)):
					LogError('File: %s, line %s, Attribute not exist!'%(playlist,line2))
				try:
					myAttr =AttrLoader(f, 0)
					if(logIntermed):
						print >>fpLog,myAttr
					
					for ftn in myAttr.ftns:
						if not ftn in FunctionList:
							FunctionList.append(ftn)
				except Exception, e:
					LogError(e)
			print >>fpLog,'FunctionList\n', FunctionList
			
			#  append to testSuite
			for ftn in FunctionList:
				ftn =ftn.replace(' ','_')
				
				file_w='%s\\TestSuite_%s.txt'%(FunctionRootPath,ftn)
				f =open(file_w,'a')
				f.writelines([line + '\n'])
				f.close()
				
		fpLog.close()
	
#root =r'\\vis_3d_pp\e$\JSHe\TestDB'	
root =sys.argv[1]
fpErrLog =open('%s\\Err.log'%(root),'w')
Main(root)
fpErrLog.close()
