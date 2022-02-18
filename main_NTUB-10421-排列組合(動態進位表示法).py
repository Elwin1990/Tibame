import sys
import math


def fun(a, n):
    list_a = list(map(int, list(a)))
    l = len(a)
    sum = 0
    q, r = 0, n-1
    for i in range(l - 1, -1, -1):
        q = r // (math.factorial(i))
        r = r % (math.factorial(i))
        sum += list_a[q] * 10**i
        del list_a[q]
    return sum


a = sys.stdin.read()
a = a.split('\n')
for i in range(int(a[0])):
    a[i + 1] = a[i + 1].split(',')
    print(fun(a[i + 1][0], int(a[i + 1][1])) + fun(a[i + 1][0], int(a[i + 1][2])))
