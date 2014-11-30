#!/usr/bin/python

import os
import fnmatch
import sys

if len(sys.argv) != 2:
    print "Wrong number of arguments"
    print "Usage compile_shaders [path to oslc]"
    sys.exit(0)

oslc_cmd = sys.argv[1]
include_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "include")
print include_dir

for root, dirname, files in os.walk("."):
    for filename in files:
        if filename.endswith(".osl"):
            print "compiling shader: " + os.path.join(root, filename)
            saved_wd = os.getcwd()
            os.chdir(root)
            retcode = os.system(oslc_cmd + " -v -I" + include_dir + ' ' + filename)
            os.chdir(saved_wd)

            if retcode != 0:
                print "Stopping because of errors..."
                sys.exit(retcode)

print "All shaders compiled!"
