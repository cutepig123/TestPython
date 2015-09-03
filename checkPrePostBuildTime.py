
def FindAndReplace(file, src, dst):
	fp = open(file,'r')
	content = fp.read()
	fp.close()
	content2 = content.replace(src, dst)
	fp = open(file,'w')
	content = fp.write(content2)
	fp.close()
	
FindAndReplace( '', r'Name="VCPreLinkEventTool"', r'Name="VCPreLinkEventTool" CommandLine="time /t >g:\1.txt"' )
FindAndReplace( '', r'Name="VCPreLinkEventTool"', r'Name="VCPreLinkEventTool" CommandLine="time /t >g:\1.txt"' )
