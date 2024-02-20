#!/bin/bash
# Use: ./bregr.sh 1.6.a

files="${1}.*.re"
input="${1}.txt"

# Example single-file workflow:
# cat 1.6.a.txt | ./regr.py 1.6.a.guerin.re

for f in $files;  do
    #echo ${f};
    cat $input | ./regr.py $f
done;
