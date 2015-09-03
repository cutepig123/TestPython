from xml.dom import minidom
import sys

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
	
xmlFile = sys.argv[1]
xmldoc = minidom.parse(xmlFile)
data = childNode(xmldoc.childNodes[0], '__data')
fp = open(xmlFile+'.txt','w')

def	FindAllTimeTag(data,baseName=""):
	for cn in data.childNodes:
		#if str(cn.__class__) != 'xml.dom.minidom.Element': continue
		
		nm = cn.nodeName
		start=childNode(cn, 'start')
		end=childNode(cn, 'end')
		
		print 'process',baseName,nm
		if start is not None:
			startTm = start.childNodes[0].nodeValue
			endTm = end.childNodes[0].nodeValue
			fp.write( "[]%s.%s:%g\n"%(baseName,nm,float(endTm) - float(startTm) ))
		
		#if len(childNodeList(cn))>0:
		FindAllTimeTag(cn,baseName+"."+nm)
FindAllTimeTag(data)
fp.close()
