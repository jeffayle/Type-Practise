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

def lineOutput(cpm, wpm, inputLine, line):
    #Figure out how many mistakes were make
    mistakes = 0
    for a, b in zip(*normalizeLengths(line,inputLine)):
        if a != b: mistakes += 1

    print "%3d CPM / %3d WPM. %d mistakes"%(cpm, wpm, mistakes) , 
    raw_input() #Wait for user to review stats
    print "" #Extra newline

def normalizeLengths(left, right):
    "Normalizes the length of two strings by appending nulls to either"
    if len(left) < len(right):
        left += "\0"*(len(right)-len(left))
    elif len(right) < len(left):
        right += "\0"*(len(left)-len(right))
    return left, right

#Startup stuff
if len(sys.argv) < 2:
    sys.stderr.write("Error: Please specify a file to practise with on the"
            "command line\n")
    exit()

#Open the file to work with
inputFile = open(sys.argv[1])

#Main loop
for line in inputFile:
    line = line.strip()
    cpm, wpm, inputLine = doLine(line)

    lineOutput(cpm, wpm, inputLine, line)
