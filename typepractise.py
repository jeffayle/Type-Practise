#!/usr/bin/env python
import time
import sys

#Startup stuff
if len(sys.argv) < 2:
    sys.stderr.write("Error: Please specify a file to practise with on the"
            "command line\n")
    exit()

#Open the file to work with
inputFile = open(sys.argv[1])
