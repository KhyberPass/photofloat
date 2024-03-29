#!/usr/bin/env python2

from TreeWalker import TreeWalker
from CachePath import message
import sys
import os

def main():
	if sys.version_info[0] < 3:
		# Ver 3 is unicode by default
		reload(sys)
		sys.setdefaultencoding("UTF-8")

	if len(sys.argv) != 3:
		print("usage: %s ALBUM_PATH CACHE_PATH" % sys.argv[0])
		return
	try:
		os.umask(0o022)
		TreeWalker(sys.argv[1], sys.argv[2])
	except KeyboardInterrupt:
		message("keyboard", "CTRL+C pressed, quitting.")
		sys.exit(-97)
	
if __name__ == "__main__":
	main()
