import commands
import os
import sys

def List(dir):
	cmd = 'ls -l ' + dir
	(status, output) = commands.getstatusoutput(cmd)
	if status:
		print 'there was and error:'
		sys.exit(1)
	print output

if __name__ == '__main__':
	List(sys.argv[1])