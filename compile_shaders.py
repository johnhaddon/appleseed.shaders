#!/usr/bin/python

import os
import fnmatch
import sys

if len(sys.argv) != 2:
    print "Wrong number of arguments"
    print "Usage compile_shaders [path to oslc]"
    sys.exit(0)

oslc_cmd = sys.argv[1]

for root, dirname, files in os.walk("."):
    for filename in files:
        if filename.endswith(".osl"):
            print "compiling shader: " + os.path.join(root, filename)
            saved_wd = os.getcwd()
            os.chdir(root)
            os.system(oslc_cmd + " -v -Iinclude " + filename)
            os.chdir(saved_wd)
