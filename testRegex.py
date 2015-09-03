import re, sys, os

infile = sys.argv[1]
outfile = infile+'new'

fw = open(outfile,'w')
for line in open(infile,'r').readlines():
	m = re.match('image ([0-9]+) = buffer', line)
	if m is None:
		fw.writelines([line])
	else:
		imgId = int(m.group(1))
		print line, imgId
		for i in range(6):
			fw.writelines(['image %d.%d = buffer%.2d.bmp\n'%(imgId,i+1,imgId)])
fw.close()