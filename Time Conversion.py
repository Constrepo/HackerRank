#https://www.hackerrank.com/challenges/time-conversion/problem

#!/bin/python3
#import sys

def timeConversion(s):
    # Complete this function
    hh,mm,ss = s.split(":")
    hInt = int(hh)
    if "AM" in ss:
        if hInt == 12:
            hh = "00"
        time = ":".join([hh,mm,ss[:2]])
        return time
    elif "PM" in ss:
        if hInt < 12:
            hInt += 12
            hh = str(hInt)
        time = ":".join([hh,mm,ss[:2]])
        return time
    else:
        time = ":".join([hh,mm,ss[:2]])
        return time

s = "12:00:25PM"
##s = input().strip()
result = timeConversion(s)
print(result)
