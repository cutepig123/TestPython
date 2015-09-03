import os,sys

def replace(file, old_str, new_str):
	print '%s %s --> %s'%(file, old_str, new_str)
	cont =open(file,'r').read()
	s=''
	if( old_str in cont ):
		s =cont.replace(old_str, new_str)
	else:
		s_con ='[Condition]'
		p =cont.find(s_con)
		assert(p>=0)
		s =cont[:(p+len(s_con))] +'\n'+new_str
	print s
	#os.system('pause')
	open(file,'w').write(s)
	
groups =[]

def GetGroupName(case_name):
	f =case_name.split('_')
	assert(len(f)>0)
	f =f[-1]
	return f
	
def	splitgroup(grp):
	idx=-1
	for i in range(len(grp)):
		if grp[i]>='0' and grp[i]<='9':
			idx =i
			break
	assert(idx>=0)
	grp_name=grp[0:idx]
	num=int(grp[idx:])
	return [grp_name, num]
	
def mapCondition(grp, num):
	B=[' Min',' Normal',' Max']
	
	M={}
	M['tra']='Translation'
	M['rot']='Rotation'
	M['sca']='Scaling'
	M['nli']='Non-linear intensity'
	M['itg']='Intensity gain'
	M['ito']='Intensity offset'
	M['uel']='Uneven lighting'
	M['dbg']='Directional blurring'
	M['def']='Defects'
	M['gno']='Gaussian noise'
	M['ibg']='Isotropic blurring'

	assert( grp in M.keys() )
	return '%s%s'%(M[grp], B[num%3])
	
def walkDir(top):
	global groups
	
	assert( os.path.isdir(top) )
	for shortName in os.listdir(top):
		fullName =os.path.join(top, shortName)
		print fullName
		fileName=os.path.join(fullName, "Attribute.txt")
		if os.path.isfile(fileName): 
			print fileName
			
			group =GetGroupName(shortName)
			[grp, num] =splitgroup(group)
			cond =mapCondition(grp, num)
			
			replace(fileName, 'Repeatability', cond)
			
			#os.system('pause')
		elif os.path.isdir(fullName): 
			walkDir(fullName)
			
folder=sys.argv[1]
walkDir(folder)
