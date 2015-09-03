import ConfigParser,os,sys
from optparse import OptionParser

def MyCmd(x):
	print ">>>",x
	os.system(x)

usage = "usage: %prog [options] dest_folder"	
parser = OptionParser(usage)
parser.add_option("-l", "--logcase", dest="logcasePath",
                  help="copy a log case with necessary repeat files" )
parser.add_option("-s", "--system", dest="copysystem",
                  help="copy system files" )
parser.add_option("-v", "--verbose",
				  action="store_true", dest="verbose")
parser.add_option("-q", "--quiet",
				  action="store_false", dest="verbose")				  

(options, args) = parser.parse_args()

#print options
#print args	
config = ConfigParser.ConfigParser()
if options.logcasePath:
	print 'parse log case',options.logcasePath
	config.read('%s\\cmdrpy.log'%(options.logcasePath))
	recid =config.get('cmd','Record ID')
	critid =config.get('cmd','Criteria ID')
	print 'get record id', recid
	dest_rec='%s\\learn\\record'
	print 'copy to',
	print 'get Criteria id', critid
	
	