import sys
import math


def fun(str1, str2):
    a, b = set(str1.split()[1:]), set(str2.split()[1:])
    print(len(a & b))


a = sys.stdin.read()
a = a.split('\n')
for x in range(int(a[0])):
    fun(a[2 * x + 1], a[2 * x + 2])
