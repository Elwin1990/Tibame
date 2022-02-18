import sys
import math

a = sys.stdin.read().splitlines()


def fun(a:str, n):
    list_a = [int(x) for x in list(a)]
    l = len(a)
    sum = 0
    q, r = 0, n-1
    for i in range(l - 1, -1, -1):
        q = r // (math.factorial(i))
        r = r % (math.factorial(i))
        yield list_a[q]
        del list_a[q]



for i in range(int(a[0])):
    a[i + 1] = a[i + 1].split(',')
    lst1 = list(fun(a[i+1][0], int(a[i+1][1])))
    lst2 = list(fun(a[i+1][0], int(a[i+1][2])))

    A = 0
    B = 0
    for j in range(len(lst1)):
        if lst1[j] == lst2[j]:
            A += 1
        if lst1[j] in lst2:
            B += 1
    print(f'{A}A{B-A}B')
