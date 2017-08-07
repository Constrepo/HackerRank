#https://www.hackerrank.com/challenges/camelcase/problem

#!/bin/python3

#import sys


#s = input().strip()
s = "saveChangesInTheEditor"
words = 1

for ltr in s:
    if ltr.isupper():
        words += 1

print(words)
