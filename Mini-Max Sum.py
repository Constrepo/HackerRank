#https://www.hackerrank.com/challenges/mini-max-sum/problem

#import sys
#arr = list(map(int, input().strip().split(' ')))

arr = list(range(1,6))

sumArr = sum(arr)

##  Longer for loop Solution:
##  sums = []
##  for n in arr:
##     sums.append(sumArr - n)

sums = [sumArr - n for n in arr]
    
print(min(sums), max(sums))
