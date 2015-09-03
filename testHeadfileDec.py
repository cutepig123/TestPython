
#1. the head file should declare:
#if !defined( ASMVISION_EAGLEAPI_CONVERT_HPP_INCLUDED )
#define	ASMVISION_EAGLEAPI_CONVERT_HPP_INCLUDED
#2. the macro name shoud be uniq

import os,sys

def CheckIfDefAndGetMacro(line):
	line2=""
	
	for i in range(len(line)):
		if line[i] == '#' or line[i] == '!' or line[i] == '('  or line[i] == ')':
			line2 += ' ' + line[i] + ' '
		else:
			line2 += line[i]
	lsp = line2.split()
	
	#print lsp, len(lsp)
	if len(lsp) == 7:
		if lsp[0]=="#" and lsp[1]=="if" and lsp[2]=="!" and lsp[3]=="defined" and lsp[4]=="(" and lsp[6]==")":
			return lsp[5]
		else:
			return None
	elif len(lsp) == 3:	#ifndef XXX
		if lsp[0]=="#" and lsp[1]=="ifndef":
			return lsp[2]
		else:
			return None
	else:
		return None
		
def CheckDefAndGetMacro(line):
	line2=""
	
	for i in range(len(line)):
		if line[i] == '#' or line[i] == '!' or line[i] == '('  or line[i] == ')':
			line2 += ' ' + line[i] + ' '
		else:
			line2 += line[i]
	lsp = line2.split()
	
	if len(lsp) != 3:
		return None
	
	if lsp[0]!="#" or lsp[1]!="define":
		return None
	
	return lsp[2]
	
def CheckAndGetMacro(filename):
	fp = open(filename, "r")
	lines = fp.readlines()
	
	#skip empty lines
	line=""
	i=0
	while i<len(lines):
		line = lines[i].strip() 
		if len(line)==0 or line.startswith('//'):
			i += 1
			continue
		else:
			break
		
	#print line
	macro = CheckIfDefAndGetMacro(line)
	if (macro is None):
		print "Cannot get ifdef"
		return None
		
	#skip empty lines
	line=""
	i += 1
	while i<len(lines):
		line = lines[i].strip() 
		if len(line)==0 or line.startswith('//'):
			i += 1
			continue
		else:
			break
		
	macro2 = CheckDefAndGetMacro(line)
	if (macro2 is None):
		print "Cannot get define"
		return None
		
	if macro != macro2:
		print macro ,"!=", macro2
		return None
		
	return macro
	
def	GetHppFileList(path):
	retfiles = []
	mymap={}
	for root, dirs, files in os.walk(path, topdown=False):	
		for name in files:	
			if name.lower().endswith(".h") or name.lower().endswith(".hpp"):
				fileName=os.path.join(root, name)
				print fileName
				macro = CheckAndGetMacro(fileName)
				if (macro is None):
					print "macro is None"
					os.system('pause')
				elif mymap.has_key(macro):
					print macro, "already Exist in ", mymap[macro]
					os.system('pause')
				else:
					mymap[macro] = fileName
					print macro
					print
				
			
	return retfiles

print GetHppFileList(r'J:\System\Project\OO Development\Implementation\CSysOO\AsmVision')	