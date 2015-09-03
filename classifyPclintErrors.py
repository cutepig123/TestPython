import os,sys

def MySplit(s,separater):
	p=0
	r=[]
	for i in range(len(separater)):
		ss =separater[i]
		p1 =0
		if i==0: #start
			p1 =s.find(ss, p)
		else:
			p1 =s.find(ss, p+len(separater[i-1]))
		if p1<0:
			return None
		#if p1>0:
		r.append(s[p:p1])
		if i==len(separater)-1:
			r.append(s[p1+len(separater[i]):])
		p =p1+len(separater[i])
	return r
	
def A():	
	
	M ={}
	for line in open(r'\\ahkex\ahkproj\VisionImaging\JSHe\pclint\solar3d.txt','r').readlines():
		#(512) : Info 732: 
		#p1  p2			 p3
		print '===>',line
		line =line.strip()
		if len(line.strip())==0: continue
		
		r =MySplit(line,['(',') : ',': '])
		#print 'return',r
		if r is None:
			#os.system('pause')
			continue
		assert(len(r)==4)
		file =r[0]
		line_num =r[1]
		type =r[2]
		cdesc =r[3]
		print '==:"%s"'%type
		assert(type.startswith('Error') or type.startswith('Info') or type.startswith('Warning'))
		if not M.has_key(type):
			M[type] ='\t'.join([file, line_num, cdesc])
			
	fp =open(r'\\ahkex\ahkproj\VisionImaging\JSHe\pclint\solar3d_log.txt','w')
	for k in M.keys():
		fp.writelines(['%s\t%s\n'%(k, M[k])])
	fp.close()
A()
		