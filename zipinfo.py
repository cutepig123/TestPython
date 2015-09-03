#! /usr/local/bin/python --
"""
usage: %(progname)s [args]
--help
[files]	-- show info of a bunch of zip files

"""

import zipfile, os, sys, getopt

def usage(progname):
	print __doc__ % vars()

def main(argv, stdout, environ):
	print argv
	progname = argv[0]
	list, args = getopt.getopt(argv[1:], "", ["help"])

	if len(args) == 0:
		usage(progname)
		return
	for (field, val) in list:
		if field == "--help":
			usage(progname)
			return
			
	for fn in args:
		print '***loading***', fn
		z = zipfile.ZipFile(fn, "r")
		for filename in z.namelist():
			bytes = z.read(filename)
			print '%10s %10d' %(filename,len(bytes))

if __name__ == "__main__":
	main(sys.argv, sys.stdout, os.environ)