#!/usr/bin/python

import os
import fnmatch
import sys

for root, dirname, files in os.walk("."):
    for filename in files:
        if filename.endswith(".oso"):
         print "removing compiled shader: " + os.path.join(root, filename)
         os.remove(os.path.join(root, filename))
