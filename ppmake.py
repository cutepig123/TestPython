#! /usr/local/bin/python

######################################################
# Author: doudehou
# Email: doudehou {at} gmail.com
# Blog: http://spaces.msn.com/yjl
# Version: 0.1
# Date & Time: 2006-03-25 00:54 AM
#
# Purpose:
# It is not easy to write Makefile which contain
# the right dependent relationship. For example,
# If you have: foo.o:foo.c
# You must specify the header files foo.c include,
# and the header files the included header files
# include, and so on. 
# By doing this, the relationship would looks like:
# foo.o:foo.c bar.h bar_include.h bar_include_include.h,..
# It is boring.
# Fortunately, GCC has a option -MM to output the
# relationship between the .o and the .c file. 
# So I write this tool to utilize this function,
# and make it automaticly.
#
# How to use:
# Just write the normal makefile as before, but now
# you don't need to list any .h files the .c/.cpp include.
# What you need to write is as simple as: foo.o:foo.c.
# And save you makefile.
# Then in the command mode, type:
# ppmake.py <Makefile_you_just_wrote> <Makefile><cr>
# the new Makefile will be outputed in <Makefile>, which
# could be any name you specified.
#
# Use make -f <Makefile> to build you project.
#
# I hope this tool will be helpful for you.:-)
# If you have any suggestion, please mail to me.
# Thank you!
######################################################

import sys
import re
import os



######################################################
if len(sys.argv) != 3:
	print "Usage: ppmake.py <input> <output>"
	sys.exit(-1)

input_name = sys.argv[1]
display_input_name = "<" + input_name + ">"

output_name = sys.argv[2]
display_output_name = "<" + output_name + ">"

temp_name = "temp.tmp"
display_temp_name = "<" + temp_name + ">"
if os.path.exists(temp_name):
	print "The temperary file", display_temp_name, "is exists,",
	print "please delete it first."
	sys.exit(-1)


######################################################

# content will contain the output string.
content = ""

# The pattern will match:
#	foo.bar:bar.foo
#	foo.bar:../bar.foo
#	foo.bar:../../bar.foo etc
# Please notes that any token started by $, #, . will
# be skipped.
pattern = "^([^$#\.].*):([^$][\w\./\\\\]+)[ |\t]*$"
re_exp = re.compile(pattern)



def process_matched_object(match_obj):
	global content
	try:
		target = match_obj.group(1)
		source = match_obj.group(2)

		command = "gcc -MM "
		command += source
		command += " >> "
		command += temp_name;
		if os.system(command) != 0:
			content += target
			content += ":"
			content += source
			content += "\n"
		else:
			temp_file = file(temp_name, "r+")
			dependent = ""
			# The output of gcc -MM could be  ... \<new line> ...
			# so I must catch this case.
			while True:
				line = temp_file.readline()
				if len(line) == 0:
					break
				dependent += line
			temp_file.close()
			content += dependent

		os.remove(temp_name)
	except:
		print display_input_name, "can't be processed",
		print "maybe something is wrong." 
		sys.exit(-1)



# The function to process a line.
def process_line(line):
	global content

	match_obj = re_exp.match(line)
	if match_obj != None:
		process_matched_object(match_obj)
	else:
		content += line



################################################### 

# Open & Read the makefile.
try:
	makefile = file(input_name, "r+")
except:
	print "The input file", display_input_name, "can't be opened!"
	sys.exit(-1)


# Preocess line by line.
while True:
	line = makefile.readline()
	if len(line) == 0:
		break
	process_line(line)
	print "\b.",


try:
	output_file = file(output_name, "w+")
	output_file.write(content)
	output_file.close()
except:
	print "The output file", display_output_name, "can't be written!"
	sys.exit (-1)

print 
print display_output_name, "has been generated successfully!"

