import re

def extractComment(fileName):
	fp = open(fileName,''r)
	content = fp.read()
	fp.close()
	comments = re.findall('(//[^\n]+|/\*[^/]+\*/)',content)
	for comment in comments:
		print '***',comment