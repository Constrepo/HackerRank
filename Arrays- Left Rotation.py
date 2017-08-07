##  https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem

def array_left_rotation(a, n, k):
    if n==len(a):
        return a[k:] + a[:k]
    else: print("The n that you entered is not equal to the\
                number of items in your list.")

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')
