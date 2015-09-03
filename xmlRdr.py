from xml.dom import minidom


def parseXml(xmlnodes,step=0):
	for i in range(0,xmlnodes.length):
		if xmlnodes[i].hasChildNodes():
			parseXml(xmlnodes[i].childNodes,step+1)
		else:
			s=''
			for j in range(0,step):s += ' '
			print s,':',xmlnodes[i].toxml().strip().replace('\n','')

xmldoc = minidom.parse('1.xml')
xmlnodes= xmldoc.childNodes
parseXml(xmlnodes)