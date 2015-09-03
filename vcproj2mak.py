#coding=utf-8

#[代码]vc2005的project==>makefile for gnumake
#发信站: 水木社区 (Wed Feb 15 14:00:02 2006), 转信
#
#习惯用vim编辑，但一些mfc的project还要用ide环境编辑，要是命令行每次自己敲也麻烦，干脆用python写了个脚本自动转化
#弄了半天，也没搞定xml中gb2312的办法，只好hard code过滤了


###########################################
# File Name: 
#	vcproj2mak
# Description: 
#   convert .vcproj file of vc2005 to makefile used by gnu make
#   suppose that we have a sample project with two configuration "Debug|Win32" and "Release|Win32"
#   the final makefile may look like:
#
# -------------------------------- makefile begin ------------------------------------------
# #----------------------------------------------------------------------------
# # makefile produced by vcproj2mak
# # author of vcproj2mak: xiaoyueer
# # author mail: xiaoyueer2000@hotmail.com
# # copyright: 2006-
# # time: Wed, 15 Feb 2006 10:49:32
# #----------------------------------------------------------------------------
# IDE:=devenv
# Project:=Demo2P
# ProjectFile:=Demo2P.vcproj
# 
# .PHONY:Debug DebugClean DebugRun DebugRunExit Release ReleaseClean ReleaseRun ReleaseRunExit all clean
# 
# all:Debug Release 
# 
# clean:DebugClean ReleaseClean 
# 
# Debug:
#	 -$(IDE) $(ProjectFile) /Project $(Project) /ProjectConfig "Debug|Win32" /Build
# 
# DebugClean:
#	 -$(IDE) $(ProjectFile) /Project $(Project) /ProjectConfig "Debug|Win32" /Clean
# 
# DebugRun:Debug
#	 -$(IDE) $(ProjectFile) /Project $(Project) /ProjectConfig "Debug|Win32" /Run
# 
# DebugRunExit:Debug
#	 -$(IDE) $(ProjectFile) /Project $(Project) /ProjectConfig "Debug|Win32" /RunExit
# 
# Release:
#	 -$(IDE) $(ProjectFile) /Project $(Project) /ProjectConfig "Release|Win32" /Build
# 
# ReleaseClean:
#	 -$(IDE) $(ProjectFile) /Project $(Project) /ProjectConfig "Release|Win32" /Clean
# 
# ReleaseRun:Release
#	 -$(IDE) $(ProjectFile) /Project $(Project) /ProjectConfig "Release|Win32" /Run
# 
# ReleaseRunExit:Release
#	 -$(IDE) $(ProjectFile) /Project $(Project) /ProjectConfig "Release|Win32" /RunExit
#  
# -------------------------------- makefile end ------------------------------------------
#  
# Usage:
#   python vcproj2mak.py sample.vcproj makefile
#
###########################################

from xml.dom import minidom
#from file_tools import file_exist, read_data
from time import localtime, strftime
import sys
import codecs
##################################################
# File Name:
#   file_tools.py
# Description:
#   file utilities
##################################################
import os
from stat import *
#import string_tools
import string

def file_exist(src):
	try:
		f = open(src, "r")
		f.close()
		return True
	except IOError:
		return False

def write_data(file, data):
	try:
		f = open(file, "w")
		f.write(data)
		f.close()
	except IOError:
		pass

def read_data(file):
	try:
		f = open(file, "r")
		data = f.read()
		f.close()
		return data
	except IOError:
		pass	



# Description:
#   get config dicts from .vcproj file
#   configuration name such as "Debug|Win32"
#   and save it in a dict, "Debug" as key and "Debug|Win32" as value
# Input:
#   prjfile: the vc project file
# Return:
#  a tuple, 
#	fist element is project_name
#	second element is a dict, for each item the key is name we used for makefile, such as "Debug", "Release"
#	the value is real name such as "Debug|Win32", "Release|Win32"	   
def getconfiginfo(data):
	#print data
	xmldoc = minidom.parseString(data)
	project = xmldoc.getElementsByTagName(r"VisualStudioProject")
	projectName = project[0].attributes["Name"].value
	config = xmldoc.getElementsByTagName(r"Configuration");
	config_dicts = {} 
	for node in config:
		value = node.attributes["Name"].value
		pos = value.find(u"|")
		key = u""
		if -1 != pos:
			key = value[0:pos]
		else:
			key = value
		config_dicts[key] = value
	return projectName, config_dicts

# Description:
#   for each configuration XXX we generate XXX, XXXClean, XXXRun, XXXRunExit
#	 XXX for build
#	 XXXClean for clean output files
#	 XXXRun for run in ide
#	 XXXRunExit for run in ide and exit automatically
#   and we generate all and clean
#	 all for build all
#	 clean for clean all
# Input:
#   config: result of getconfiginfo, see above
#   project_file: .vcproj file of vc2005
#   dstfile: make file to generate
def buildmakefile(config, project_file, dstfile):
	project_name = config[0]
	config_dict = config[1]
	strCurTime = strftime("%a, %d %b %Y %H:%M:%S", localtime())
	strFileHeader = '#----------------------------------------------------------------------------\n\
# makefile produced by vcproj2mak\n\
# author of vcproj2mak: xiaoyueer\n\
# author mail: xiaoyueer2000@hotmail.com\n\
# copyright: 2006-\n\
# time: ' + strCurTime + '\n\
#----------------------------------------------------------------------------\n'
	dst = open(dstfile, "w")
	dst.write(strFileHeader)
	strHeader = "IDE:=devenv\nProject:=" + project_name + "\nProjectFile:=" + project_file + "\n"
	dst.write(strHeader)
	dst.write("\n")
	dst.write(".PHONY:")
	str_all = "all:"
	str_clean = "clean:"
	for cfg in config_dict.keys():
		str_all += cfg + " "
		str_clean += cfg + "Clean "
		dst.write(cfg + " ")
		dst.write(cfg + "Clean ")
		dst.write(cfg + "Run ")
		dst.write(cfg + "RunExit ")
	
	dst.write("all clean\n")
	dst.write("\n" + str_all + "\n")
	dst.write("\n" + str_clean + "\n")
	strLineHeader = "-$(IDE) $(ProjectFile) /Project $(Project) /ProjectConfig \""; 
	for item in config_dict.items():
		dst.write("\n")
		dst.write(item[0] + ":\n\t")
		dst.write(strLineHeader + item[1] + "\" /Build\n")
		dst.write("\n")
		dst.write(item[0] + "Clean:\n\t")
		dst.write(strLineHeader + item[1] + "\" /Clean\n")
		dst.write("\n")
		dst.write(item[0] + "Run:" + item[0] + "\n\t")
		dst.write(strLineHeader + item[1] + "\" /Run\n")
		dst.write("\n")
		dst.write(item[0] + "RunExit:" + item[0] + "\n\t")
		dst.write(strLineHeader + item[1] + "\" /RunExit\n")
	dst.close()

def vcproj2mak(srcfile, dstfile):
	config = getconfiginfo(preprocess(srcfile))
	buildmakefile(config, srcfile, dstfile)

# remove encoding="gb2312"
def preprocess(srcfile):
	#data = read_data(srcfile).encode('utf-8')
	# if None == data:
		# raise IOError, "can't open " + srcfile

	f = codecs.open(srcfile,'rb','mbcs')
	data = f.read().encode('utf-8')
	f.close
	return data.replace('encoding="gb2312"?', '?')

def _vcprojmain():   
	if (len(sys.argv) == 3):
		prj_file = sys.argv[1]
		dst_file = sys.argv[2]
		if file_exist(dst_file):
			action = raw_input(dst_file + " exists, overwrite?(Yes/No)").lower()
			if (action[0] == 'n'):
				return
	else:
		print "usage: " + sys.argv[0] + " prjfile" + " makefile"
		return

	#try:
	vcproj2mak(prj_file, dst_file)
	print "convert successfully"
	#except:
	#	print "conver error"

if __name__ == '__main__':
	_vcprojmain()


