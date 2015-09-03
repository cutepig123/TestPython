from xml.dom import minidom
import os,sys

def childNodeList(x,tagName = None):
	CNs=[]
	#if str(x.__class__) == 'xml.dom.minidom.Element':
	try:
		for cn in x.childNodes:
			if tagName is None or cn.nodeName == tagName:
				CNs.append(cn) 
	except:
		pass
	return CNs
	
def childNode(x,tagName = None):
	#if str(x.__class__) == 'xml.dom.minidom.Element':
	try:
		for cn in x.childNodes:
			if tagName is None or cn.nodeName == tagName:
				return (cn) 
	except:
		pass
		
	return None
	
	
class	MarkSummary:
	def	__init__(self):
		self.MarkStatus="NC"
		self.SHAStatus="NC"
		self.QualityStatus="NC"
		self.ExtraStatus="NC"
		self.BrokenStatus="NC"
		self.numOfQualityRejected=0
		self.QualityRejected=''
		self.numOfSklRejected=0
		self.maxExtraStrokeLength=0
		self.maxBrokenStrokeLength=0
		self.numOfCharRejected=0
		self.CharRejected=''
		
	#return 1:should check char, 0 need not check char
	def Hdr(self):
		return ['SHAStatus','QualityStatus','ExtraStatus','BrokenStatus',
			'numOfQualityRejected','numOfSklRejected','numOfCharRejected',
			'QualityRejected','CharRejected','maxExtraStrokeLength','maxBrokenStrokeLength']
	def Value(self):
		return [self.SHAStatus,self.QualityStatus,self.ExtraStatus,self.BrokenStatus,
			str(self.numOfQualityRejected),str(self.numOfSklRejected),str(self.numOfCharRejected),
			self.QualityRejected,self.CharRejected,str(self.maxExtraStrokeLength),str(self.maxBrokenStrokeLength)]
	
	def	chkMarkStatus(self,markStatus):
		self.MarkStatus = markStatus
		if markStatus=="YES":
			return 1
		else:
			return 0
	def _chkCharStatus(self,selfCharStatus,charStatus):
		if not (selfCharStatus=="NC" or selfCharStatus=="YES" or selfCharStatus=="NO" or selfCharStatus=="-1" or selfCharStatus=="-2" or selfCharStatus=="0" or selfCharStatus=="1"):
			print 'Error',selfCharStatus
			assert(0)
		if selfCharStatus=="NC" or selfCharStatus=="-2":
			selfCharStatus=charStatus
		elif charStatus=="NO" or charStatus=="-1":
			selfCharStatus=charStatus
		return selfCharStatus
		
	def	chkCharStatus(self,charInfo):
		self.SHAStatus = self._chkCharStatus(self.SHAStatus,charInfo.SHAStatus)
		self.QualityStatus = self._chkCharStatus(self.QualityStatus,charInfo.QualityStatus)
		self.ExtraStatus = self._chkCharStatus(self.ExtraStatus,charInfo.ExtraStatus)
		self.BrokenStatus = self._chkCharStatus(self.BrokenStatus,charInfo.BrokenStatus)
		if charInfo.QualityStatus=='-1' or charInfo.SHAStatus=='NO':
			self.numOfQualityRejected += 1
			self.QualityRejected += ',%s'%(charInfo.ID)
		if charInfo.QualityStatus=='-1' or charInfo.SHAStatus=='NO' or charInfo.ExtraStatus=='-1' or charInfo.BrokenStatus=='-1':
			self.numOfCharRejected += 1
			self.CharRejected += ',%s(%s)'%(charInfo.ID,charInfo.QualityScore)
		if charInfo.SHAStatus=='NO' or charInfo.ExtraStatus=='-1' or charInfo.BrokenStatus=='-1':
			self.numOfSklRejected +=1
		try:
			self.maxBrokenStrokeLength = max(self.maxBrokenStrokeLength,float(charInfo.BrokenLength))
			self.maxExtraStrokeLength = max(self.maxExtraStrokeLength,float(charInfo.ExtraLength))
		except Exception,e:
			print "Expt in chkCharStatus",e
			
	# def chkMarkCharStatus(self,markReader):
		# self.chkMarkStatus(markReader.MarkStatus)
		# for charInfo in markReader.arrayCharMapInfo:
			# self.chkCharStatus(charInfo)
	def printStatus(self)	:
		print '\t'.join(['MarkStatus','SHAStatus','QualityStatus','ExtraStatus','BrokenStatus'])
		print '\t'.join([self.MarkStatus,self.SHAStatus,self.QualityStatus,self.ExtraStatus,self.BrokenStatus])
	
	def printTBStatus(self)	:
		print "<table border=1>"
		print '<tr><td>','</td><td>'.join(['MarkStatus','SHAStatus','QualityStatus','ExtraStatus','BrokenStatus']),'</td></tr>'
		print '<tr><td>','</td><td>'.join([self.MarkStatus,self.SHAStatus,self.QualityStatus,self.ExtraStatus,self.BrokenStatus]),'</td></tr>'
		print "</table>"
		
class 	CharInfo:
	def __init__(self,xmlMap,pathLocal,PathJ):
		self.pathLocal=pathLocal
		self.PathJ=PathJ
		self.ID=''
		self.SHAScore=''
		self.QualityStatus='-2'
		self.QualityScore=''
		self.fromMap(xmlMap)
		
	def fromMap(self,xmlMap):
		self.Type = xmlMap['Type']
		self.SHAStatus=xmlMap['Presence']
		if xmlMap.has_key('Alignment Score'):
			self.SHAScore=xmlMap['Alignment Score']
		if xmlMap.has_key('Quality Score_LV'):
			self.QualityStatus=xmlMap['Quality Score_LV']
		if xmlMap.has_key('Quality Score'):
			self.QualityScore=xmlMap['Quality Score']
		self.ExtraStatus=xmlMap['Extra Length_LV']
		self.ExtraLength=xmlMap['Extra Length']
		self.BrokenStatus=xmlMap['Broken Length_LV']
		
		self.BrokenLength=xmlMap['Broken Length']
		self.idx=xmlMap['idx']
		if xmlMap.has_key('ID'):
			self.ID=xmlMap['ID']
		
		
	def Hdr(self):
		return ['pathLocal','PathJ','idx','ID','Type','SHAStatus','SHAScore','QualityStatus','QualityScore','ExtraStatus','ExtraLength','BrokenStatus','BrokenLength']
	def Value(self):
		return [mkAHref(self.pathLocal),mkAHref(self.PathJ),self.idx,self.ID,self.Type,self.SHAStatus,self.SHAScore,self.QualityStatus,self.QualityScore,self.ExtraStatus,self.ExtraLength,self.BrokenStatus,self.BrokenLength]
		
	def printHdr(self):
		print '=\t'.join(self.Hdr())
		
	def printValue(self):
		print '=\t'.join(self.Value())
	
	def printTRHdr(self):
		print '<tr><td>','</td><td>'.join(self.Hdr()),'</td></tr>'
	def writeToFileTRHdr(self,fp):
		fp.writelines(['<tr><td>','</td><td>'.join(self.Hdr()),'</td></tr>\n'])
		
	def printTRValue(self):
		print '<tr><td>','</td><td>'.join(self.Value()),'</td></tr>'
	
	def writeToFileTRValue(self,fp):
		fp.writelines(['<tr><td>','</td><td>'.join(self.Value()),'</td></tr>\n'])
		
	def getStatus(self,selfCharStatus):
		if selfCharStatus=="NC" or selfCharStatus=="-2":
			return "-2"
		elif selfCharStatus=="NO" or selfCharStatus=="-1":
			return "-1"
		elif selfCharStatus=="YES" or selfCharStatus=="0":
			return "0"
		else:
			assert(0)
	
def ReadErrReport(pathLocal,fileName='ErrReport.xml'):
	xmlFile=os.path.join(pathLocal, fileName)
	if not  os.path.isfile(xmlFile):return None
	try:
		xmldoc = minidom.parse(xmlFile)
	except:
		print "Error parse " ,fileName
		return None
	assert(xmldoc.childNodes[0].nodeName==r'TestCaseReport' and xmldoc.childNodes[0].hasChildNodes())
	pathLocal_j={}
	for errorCase in xmldoc.childNodes[0].childNodes:
		if not('Error'==errorCase.nodeName and errorCase.hasChildNodes()):continue
		pathLocal=''
		pathJ=''
		for error_prop in errorCase.childNodes:
			if error_prop.nodeName=='target' and error_prop.hasChildNodes():
				pathLocal=error_prop.childNodes[0].nodeValue
				pathLocal=pathLocal.split('\\')[-1]
			elif error_prop.nodeName=='source' and error_prop.hasChildNodes():
				pathJ=error_prop.childNodes[0].nodeValue
		if 	pathLocal!='':
			pathLocal_j[pathLocal]=pathJ
			print pathLocal,pathJ
	return pathLocal_j
def 	mkAHref	(s,maxLen=10):
	return '<a href=%s>%s</a>'%(s,s[-10::])
	

	
class	MarkReader:
	def __init__(self,pathLocal,pathJ):
		self.pathLocal=pathLocal
		self.pathJ=pathJ
		self.arrayCharMapInfo=[]	#map
		self.arrayCharInfo=[]		#class
		self.MarkStatus="NC"
		self.markSummary=MarkSummary()
		self.tmplName=''
		self.tmplId='-1'
	def Hdr(self):
		return ['pathLocal','pathJ','MarkStatus','tmplName','tmplId']
	def Value(self):
		return ['<a href=%s>%s</a>'%(self.pathLocal,self.pathLocal),'<a href=%s>%s</a>'%(self.pathJ,self.pathJ[-10::]),self.MarkStatus,self.tmplName,self.tmplId]
		
	def writeMarkSummaryHdrToFile(self,fp):
		fp.writelines(['<tr><td>','</td><td>'.join(self.Hdr()+self.markSummary.Hdr()),'</td></tr>\n'])
	def writeMarkSummaryToFile(self,fp):
		fp.writelines(['<tr><td>','</td><td>'.join(self.Value()+self.markSummary.Value()),'</td></tr>\n'])
		
	def	FindMarkNode(self,inspItem):
		mark=None
		if (inspItem.attributes) is not None and inspItem.attributes.items()==[(u'type', u'Mark Inspection')]:
			mark=inspItem
			#break
			if mark is None: return
			assert(mark.attributes.items()==[(u'type', u'Mark Inspection')])
			#self.MarkStatus="NO"
			if self.MarkStatus=="NO":return
			
			for char in mark.childNodes:
				if char.nodeName=='pty':
					if char.attributes.items()==[(u'name', u'Template Name')]:
						tmplName=char
						if tmplName.childNodes[0].hasChildNodes():
							self.tmplName=tmplName.childNodes[0].childNodes[0].nodeValue
					elif char.attributes.items()==[(u'name', u'Template ID')]:
						tmplID=char
						self.tmplId=tmplID.childNodes[0].childNodes[0].nodeValue 
					elif char.attributes.items()==[(u'name', u'Presence')]:
						Present=char
						self.MarkStatus=Present.childNodes[0].childNodes[0].nodeValue 
				elif char.nodeName=='obj':	#<obj type="Character" idx="3">
					assert(len(char.attributes.items())==2)
					assert(char.attributes.items()[0]==(u'type', u'Character'))
					idx = char.attributes['idx'].value
					#s=idx
					charInfo={}
					charInfo['idx']=(idx)
					
					for charProp in char.childNodes:	#<pty name="??">
						#assert(charProp.attributes.items()==[(u'name', u'Presence')])
						if  charProp.attributes is None: continue
						
						assert(charProp.attributes.items()[0][0]==u'name')
						propName=charProp.attributes.items()[0][1]
						
						assert(charProp.childNodes[0].nodeName == u'ptyVal')
						if len(charProp.childNodes[0].childNodes)>0:
							propVal=charProp.childNodes[0].childNodes[0].nodeValue
						else:
							propVal=''
							
						assert(charProp.childNodes[1].nodeName == u'ptyAL')
						if len(charProp.childNodes[1].childNodes)>0:
							propAcceptLv=charProp.childNodes[1].childNodes[0].nodeValue
						else:
							propAcceptLv=''
						
						charInfo[propName]=propVal
						charInfo[propName+"_LV"]=propAcceptLv
					self.arrayCharMapInfo.append(charInfo)
					ci=CharInfo(charInfo,self.pathLocal,self.pathJ)
					self.arrayCharInfo.append(ci)
					self.markSummary.chkCharStatus(ci)
		else:
			for inspItemC in inspItem.childNodes:
				self.FindMarkNode(inspItemC)
				
	def ReadMarkResult(self,xml_file_name='result.xml'):
		try:
			xmldoc = minidom.parse(os.path.join(self.pathLocal, xml_file_name))
		except:
			print "Error parse " ,fileName
			return 
		assert(xmldoc.childNodes[0].nodeName=='result' and xmldoc.childNodes[0].hasChildNodes())
		assert(xmldoc.childNodes[0].childNodes[0].nodeName == 'heading')
		assert(xmldoc.childNodes[0].childNodes[1].nodeName == 'obj')
		
		for inspItem in xmldoc.childNodes[0].childNodes[1].childNodes:
			self.FindMarkNode(inspItem)
		#srch mark
		
	def printSelectedChars(self,func=lambda charInfo:charInfo.getStatus(charInfo.QualityStatus)=="-1"):
		for charInfo in self.arrayCharInfo:
			if func(charInfo):
				charInfo.printTRValue()
				
	def writeToFileSelectedChars_BySummary(self,fp,func):
		if func(self.markSummary):
			for charInfo in self.arrayCharInfo:
				charInfo.writeToFileTRValue(fp)

	def writeToFileSelectedChars(self,fp=sys.stdout,func=lambda charInfo:charInfo.getStatus(charInfo.QualityStatus)=="-1"):
		for charInfo in self.arrayCharInfo:
			if func(charInfo):
				charInfo.writeToFileTRValue(fp)

def  processAll():
	mList = os.listdir('./')
	for mPath in mList:
		xmlfile=os.path.join(mPath,'result.xml')
		if  os.path.isfile(xmlfile):
			pass
		elif mPath=='result.xml':
			mPath='./'
		else:continue
		
		print mPath
		MR=MarkReader(mPath)
		MR.ReadMarkResult()
		
		print len(MR.arrayCharInfo)
		#continue
		isPrintHdr=1
		isPrintTRValue=1
		print '<table border=1>'
		for ci in MR.arrayCharInfo:
			if isPrintHdr==1:
				ci.printTRHdr()
				isPrintHdr=0
			
			if isPrintTRValue==1:
				ci.printTRValue()
		print '</table>'
		MR.markSummary.printTBStatus()
		
def  processSelectedCase(fp,ErrorReport,func,PrintHdrFunc=None):
	mList = os.listdir('./')
	fp.writelines(['<table border=1>\n'])
	isPrintTRHdr=1
	
	for mPath in mList:
		if not os.path.isdir(mPath):continue
		xmlfile=os.path.join(mPath,'result.xml')
		if  os.path.isfile(xmlfile):
			pass
		elif mPath=='result.xml':
			mPath='./'
		else:continue
		print mPath,
		
		PathJ=''
		pathLocal=mPath.split('\\')[-1]
		if ErrorReport is not None:
			if ErrorReport.has_key(pathLocal):
				PathJ=ErrorReport[pathLocal]
		
		#print mPath
		MR=MarkReader(mPath,PathJ)
		MR.ReadMarkResult()
		
		#print len(MR.arrayCharInfo)
		#continue
		nChars=len(MR.arrayCharInfo)
		if nChars>0:
			print '[OK]',nChars,'Chars'
		else:
			print '[NO CHAR]'
			
		if isPrintTRHdr:
			if PrintHdrFunc is None:
				if nChars>0:
					MR.arrayCharInfo[0].writeToFileTRHdr(fp)
					isPrintTRHdr=0
			else:
				PrintHdrFunc(MR,fp)
				isPrintTRHdr=0
		func(MR)
		#MR.writeToFileSelectedChars(fp,func)
		
		#MR.markSummary.printTBStatus()		
	fp.writelines(['</table>\n'])

def QualityNotEquSkl(charInfo):
	sklStatus=charInfo.getStatus(charInfo.ExtraStatus)
	if charInfo.getStatus(charInfo.BrokenStatus)=='-1':sklStatus='-1'
	return sklStatus!=charInfo.getStatus(charInfo.QualityStatus) and (sklStatus=='0' or sklStatus=='-1')
def QualityFailSklPass(charInfo):
	sklStatus=charInfo.getStatus(charInfo.ExtraStatus)
	if charInfo.getStatus(charInfo.BrokenStatus)=='-1':sklStatus='-1'
	return '-1'==charInfo.getStatus(charInfo.QualityStatus) and sklStatus=='0'
def QualityPassSklFail(charInfo):
	sklStatus=charInfo.getStatus(charInfo.ExtraStatus)
	if charInfo.getStatus(charInfo.BrokenStatus)=='-1':sklStatus='-1'
	return '0'==charInfo.getStatus(charInfo.QualityStatus) and sklStatus=='-1'
	
print	'===result.xml Logging Tools==='
print	'Please select action:'
print	'\t1:Quality Fail'
print	'\t2:Quality Pass'
print	'\t3:All'
print	'\t4:SummarySHAAndQualityPass'
print	'\t5:Quality!=Skl'
print	'\t6:QualityFailSklPass'
print	'\t7:QualityPassSklFail'
print	'\t8:Summary Status of all mark'


method=int(raw_input(''))
fileName='%d.htm'%(method)
while os.path.isfile(fileName):
	fileName=raw_input("Input logging file name:\n")
	if os.path.isfile(fileName):
		print 'File',fileName,'exists! pls select another name'
	else:break
	
fp=open(fileName,'w')#sys.stdout
ErrorReport=ReadErrReport('./','ErrReport2.xml')
if (ErrorReport is None):
	ErrorReport=ReadErrReport('./','ErrReport.xml')
if (ErrorReport is not None):
	print 'Load errorreport','OK'
else:
	print 'Load errorreport','FAIL'
if method==1:
	processSelectedCase(fp,ErrorReport,lambda MR: MR.writeToFileSelectedChars(fp,lambda charInfo:charInfo.getStatus(charInfo.QualityStatus)=="-1" )) #and charInfo.Type=='Char'
elif method==2:
	processSelectedCase(fp,ErrorReport,lambda MR: MR.writeToFileSelectedChars(fp,lambda charInfo:charInfo.getStatus(charInfo.QualityStatus)!="-1"))
elif method==3:
	processSelectedCase(fp,ErrorReport,lambda MR: MR.writeToFileSelectedChars(fp,lambda charInfo:1))
elif method==4:
	processSelectedCase(fp,ErrorReport,lambda MR: MR.writeToFileSelectedChars_BySummary(fp,lambda charSummary:charSummary.QualityStatus=="0" and charSummary.SHAStatus=="YES"))
elif method==5:
	processSelectedCase(fp,ErrorReport,lambda MR: MR.writeToFileSelectedChars(fp,QualityNotEquSkl))
elif method==6:
	processSelectedCase(fp,ErrorReport,lambda MR: MR.writeToFileSelectedChars(fp,QualityFailSklPass))
elif method==7:
	processSelectedCase(fp,ErrorReport,lambda MR: MR.writeToFileSelectedChars(fp,QualityPassSklFail))
elif method==8:
	processSelectedCase(fp,ErrorReport,lambda MR: MR.writeMarkSummaryToFile(fp),lambda MR,fp:MR.writeMarkSummaryHdrToFile(fp))
			