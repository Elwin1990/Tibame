import sys
import math


def fun(str1, str2):
    a, b = set(str1), set(str2)
    check = 0
    for i in range(97,123):
        if chr(i) in (a & b):
            print(chr(i), end='')
            check = 1
    if check == 0:
        print('N')
    else:
        print('')

a = sys.stdin.read()
a = a.split('\n')
for x in range(int(a[0])):
    fun(a[2*x + 1], a[2*x + 2])

