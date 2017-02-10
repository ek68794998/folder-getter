import os
import re
import datetime

rootDir = 'C:\\Windows'

def printDirs(rootDir, depth = 0):
	rootLength = len(re.split('[\\\\/]', rootDir));

	for root, dirs, files in os.walk(rootDir):
		dirs.sort()
		files.sort()

		path = re.split('[\\\\/]', root)
		pathLength = len(path) - rootLength + 1

		print (depth + pathLength - 1) * '\t', os.path.basename(root)

		for fname in files:
			fullPath = os.path.join(root, fname)

			try:
				(mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(fullPath)
				modTime = datetime.datetime.fromtimestamp(mtime).strftime("%Y/%m/%d %H:%M:%S")
			except:
				size = 0
				modTime = datetime.datetime.fromtimestamp(0).strftime("%Y/%m/%d %H:%M:%S")

			print (depth + pathLength) * '\t', '%s\t\t%d\t%s' % (fname, size, modTime)

print "Printing files and directories in", rootDir
printDirs(rootDir)
