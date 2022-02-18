import sys
import math


def fun(str1):
    str2 = str1.split(',')
    a, b = eval(str2[0]), eval(str2[1])
    check = 'Y'
    if abs(a - b) == 2:
        for i in range(2, math.ceil(a**0.5)):
            if a % i == 0:
                check = 'N'
                break
        if check == 'Y':
            for i in range(2, math.ceil(b**0.5)):
                if b % i == 0:
                    check = 'N'
                    break
    else:
        check = 'N'
    print(check)


a = sys.stdin.read()
a = a.split('\n')
for x in range(int(a[0])):
    fun(a[x + 1])
