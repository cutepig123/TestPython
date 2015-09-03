from xml.dom import minidom
import sys

def childNodeList(x,tagName = None):
	CNs=[]
	if str(x.__class__) == 'xml.dom.minidom.Element':
		for cn in x.childNodes:
			if tagName and cn.nodeName == tagName:
				CNs.append(cn) 

	return CNs
	
def childNode(x,tagName = None):
	if str(x.__class__) == 'xml.dom.minidom.Element':
		for cn in x.childNodes:
			if tagName and cn.nodeName == tagName:
				return (cn) 

	return None
	
xmlFile = sys.argv[1]
xmldoc = minidom.parse(xmlFile)
data = childNode(xmldoc.childNodes[0], '__data')
fp = open(xmlFile+'.txt','w')

for cn in data.childNodes:
	if str(cn.__class__) != 'xml.dom.minidom.Element': continue
	nmBase = cn.nodeName
	for cncn in cn.childNodes:
		nm = cncn.nodeName
		#print nmBase,nm,
		#print cncn.childNodes
		start=childNode(cncn, 'start')
		end=childNode(cncn, 'end')
		
		if start is not None:
			startTm = start.childNodes[0].nodeValue
			endTm = end.childNodes[0].nodeValue
			fp.write( "[]%s_%s:%g\n"%(nmBase,nm,float(endTm) - float(startTm) ))

fp.close()
