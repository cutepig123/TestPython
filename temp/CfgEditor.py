import os,sys
# -add folder file section field
# -delete folder file section field
# -modify folder file section field field_new	#support \n

def	EditCfg( op, file, section, field, field_new)
	cur_section=''
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