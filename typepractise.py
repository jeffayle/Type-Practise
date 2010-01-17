#!/usr/bin/env python
import time
import sys

#Functions
def doLine(line):
    "Times the typing speed of a line. Returns (CPM, WPM, line entered)"
    pass

#Startup stuff
if len(sys.argv) < 2:
    sys.stderr.write("Error: Please specify a file to practise with on the"
            "command line\n")
    exit()

#Open the file to work with
inputFile = open(sys.argv[1])

#Main loop
for line in inputFile:
    cpm, wpm, inputLine = doLine(line)
