# regr - Regular Expression Tester

Command-line regular expression tester. Designed originally for my Theory of Computation class.

While I'm sure other options exist, at the point I wrote this I looked around the Internet and wasn't satisfied with the options I found so I wrote a couple of quick scripts to do the job.

Input/output format are designed to correspond closely to those used by [JFLAP](https://www.jflap.org/), since I currently use JFLAP for other forms of automata for assignments. I didn't like how JFLAP handled regular expressions, so coming up with an auxiliary tool made sense.

## Use

The two tools are [regr](./regr.py) and [bregr](./bregr.sh). The former handles a single regular expression and the second allows easy batch processing of one or more regular expressions (e.g., multiple submissions of a problem in an assignment).

### Input File Formats

## Regular Expressions
Test files are designed for quick pattern matching in their names. E.g., problem 1.a, submission by Guerin would be [1.a.guerin.re](./test/1.a.guerin.re). Many such test files can be ran against a single test file (e.g., one for each student in a class for that problem).

Each regular expression file (.re) should contain a single line consisting of a regular expression in plaintext format.

## Test files
A corresponding *test* to 1.a.name.re would be [1.a.txt](./test/1.a.txt). Several .re files can be ran against a single .txt file containing test cases.

### regr - REGular expression testeR

### bregr - Batch REGular expression testeR


