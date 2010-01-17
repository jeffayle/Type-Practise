#!/usr/bin/env python
from time import time
import sys

#Functions
def doLine(line):
    "Times the typing speed of a line. Returns (CPM, WPM, line entered)"
    print line
    startTime = time()
    inputLine = raw_input()
    endTime = time()

    #time it took to enter line, in minutes
    dtime = (endTime - startTime)/60
    cpm = len(line) / dtime
    wpm = len(line.split(" ")) / dtime

    return cpm, wpm, inputLine

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
