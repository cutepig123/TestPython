import os,sys

for case in open(sys.argv[1],'r').readlines():
	case =case.strip()
	if len(case)==0:continue
	if case[0]=='#':continue
	if not os.path.isdir(case):
		print 'Err not dir', case
		continue
	cmdrpy =os.path.join(case,'cmdrpy.log')
	if not os.path.isfile(cmdrpy):
		print 'Err not file', cmdrpy
		continue
	