##  https://www.hackerrank.com/challenges/ctci-making-anagrams/problem

def number_needed(a, b):
    num = 0
    setc=sorted(set(a+b))

    for x in setc:
        acount, bcount = a.count(x), b.count(x)
        num += abs(acount - bcount)

    return num

a = input().strip()
b = input().strip()

print(number_needed(a, b))
