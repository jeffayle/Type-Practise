#!/usr/bin/env python
# Copyright (c) 2010, Jeffrey Aylesworth <jeffrey@aylesworth.ca>
# 
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
# 
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# http://github.com/jeffayle/Type-Practise

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
