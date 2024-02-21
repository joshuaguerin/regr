# regr - Regular Expression Tester

Command-line regular expression tester. Designed originally for my Theory of Computation class.

While I'm sure other options exist, at the point I wrote this I looked around the Internet and wasn't satisfied with the options I found so I wrote a couple of quick scripts to do the job.

Input/output format are designed to correspond closely to those used by [JFLAP](https://www.jflap.org/), since I currently use JFLAP for other forms of automata for assignments. I didn't like how JFLAP handled regular expressions, so coming up with an auxiliary tool made sense.

## Use

The two tools are [regr](./regr.py) and [bregr](./bregr.sh). The former handles a single regular expression and the second allows easy batch processing of one or more regular expressions (e.g., multiple submissions of a problem in an assignment).

Note that `bregr` requires `regr`, so you must have *both* in the working directory for use.

### Input File Formats

## Regular Expressions
Test files are designed for quick pattern matching in their names. E.g., problem 1.a, submission by Guerin would be [1.a.guerin.re](./test/1.a.guerin.re). Many such test files can be ran against a single test file (e.g., one for each student in a class for that problem).

Each regular expression file (.re) should contain a single line consisting of a regular expression in plaintext format.

## Test files
A corresponding *test* to 1.a.name.re would be [1.a.txt](./test/1.a.txt). Several .re files can be ran against a single .txt file containing test cases.

Each line of a test file should contain a string to be matched, and either the word `Accept` or `Reject` corresponding to acceptance of the string. There is no specific ordering requirement of lines, but I will often order them lexicographically for convenience.

A sample test file could look like:
```
 Accept
0 Reject
1 Reject
01 Reject
10 Reject
11 Accept
0100 Reject
1001 Reject
1111 Accept
111110 Reject
111111 Accept
1001101 Accept
11111111 Accept
```

## bregr - Batch REGular expression testeR

`bregr.sh` is a bash script that automates the workflow by:
1. Finding all .re files that match a given prefix and
2. Running those against a test file using regr.

This script is the easier of the two to use, and is likely a good starting point if you don't know which script fits your use case.

If a problem and its associated files begin with the prefix `1.a`, then it will pull all files with that prefix and the .re suffix for testing.

Example use:
```
./bregr.sh test/1.a
```

should generate:
```
test/1.a.guerin.re (11)*
** Accept 
*0* Reject 
*1* Reject 
*01* Reject 
*10* Reject 
*11* Accept 
*0100* Reject 
*1001* Reject 
*1111* Accept 
*111110* Reject 
*111111* Accept 
*1001101* Accept (Reject)
*11111111* Accept 
```

If more files were in the test directory containing the prefix `1.a` (for other students), `bregr` should process them all.

For testing purposes, `bregr` should provide the most convenience for the user.


## regr - REGular expression testeR

This utility is designed to take a regular expression file as a command-line argument, and parses stdin for test cases until an end of text input is encountered (e.g., `ctrl+d`).

E.g., The following is a sample interaction of the program with data from stdin. The command:
```
./regr.py ./test/1.a.guerin.re
```

should generate:

```
./test/1.a.guerin.re (11)*
 Reject
** Reject (Accept)
11 Accept
*11* Accept 
101 Reject
*101* Reject 
1101 Accept
*1101* Accept (Reject)
```

The first line of output consists of the file name and the contents, and each pair of lines that result contain first the test case, then the result. In output, strings are surrounded by asterisks to make visual parsing easier (e.g., the empty string above is printed as \*\*). If the Accept/Reject matches expectation it is printed. If it fails to match expectations, the result also shows expected output.

Since input is from standard in, `cat` and a pipe can be used to input file test data.

The command:
```
cat ./test/1.a.txt | ./regr.py ./test/1.a.guerin.re
```

should generate:

```
./test/1.a.guerin.re (11)*
** Accept 
*0* Reject 
*1* Reject 
*01* Reject 
*10* Reject 
*11* Accept 
*0100* Reject 
*1001* Reject 
*1111* Accept 
*111110* Reject 
*111111* Accept 
*1001101* Accept (Reject)
*11111111* Accept 
```

## Issues
This is a pretty quick and dirty script. It is currently working well for its intended purpose, which is automating regular expression testing for homework assignments. Since it is matching patterns in names, student work can easily be pulled from repos and dumped into a single directory for testing purposes.

If you discover any major issues that you wish to report, feel free to create an issue. Since things are currently working well enough to make my life easier I'm not certain if or how this repo will be updated.
