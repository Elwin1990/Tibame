import sys
import math


def fun(str1):
    str2 = str1.split(',')
    a, b, c, d = int(str2[0]), int(str2[1]), int(str2[2]), int(str2[3])
    x = (a*c-d)//(c-b)
    print(f'{x},{a-x}')

a = sys.stdin.read()
a = a.split('\n')
for x in range(int(a[0])):
    fun(a[x + 1])
