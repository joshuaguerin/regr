#!/usr/bin/env python3

import sys # argv, stdin
import re

# Check file parameter
argc = len(sys.argv)
if argc < 2:
    print("Error: No file specified")
    exit()

file_name = sys.argv[1]
    
# Get regular expression
regfile = open(file_name, "r")
reg = regfile.readline()
regfile.close()

# Trailing newline
reg = reg.rstrip()

print(file_name, reg)

for line in sys.stdin:
    (string, tag) = line.split(' ')
    tag = tag.rstrip()

    m = re.match(reg, string)

    # Remove false positives
    if m and m.group() != string:
        m = None

    # Print test information
    print('*', string, '* ', tag, sep='', end=' ')
    
    # Terminate line with appropriate success or failure
    if m==None and tag=="Accept":
        print("(Reject)")
    elif m and tag=="Reject":
        print("(Accept)")
    else:
        print()
        
    
