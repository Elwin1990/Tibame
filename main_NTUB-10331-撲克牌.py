import sys
import math


def mod13(a):
    return a % 13


def fun(str1):
    a = sorted(list(map(int, str1.split())))
    b = sorted(list(map(mod13, a)))
    color = []
    for i in range(2):
        # 同花順
        if (a[i] % 13 < 10) and (a[i] + 4 == a[i + 4]):
            return 7
    for i in range(4):
        if (a[i] % 13 == 10) and ((a[i] - 9) in a):
            return 7
    # 鐵支
    for i in range(13):
        color.append(b.count((i + 1) % 13))
        if color[i] == 4:
            return 6
    # 葫蘆
    if (3 in color) and (2 in color):
        return 5
    # 順子
    for i in range(9):
        if color[i] * color[i + 1] * color[i + 2] * color[i + 3] * color[
                i + 4] > 0:
            return 4
    if color[9] * color[10] * color[11] * color[12] * color[0] > 0:
        return 4
    # 三條
    if 3 in color:
        return 3
    # 兩對
    if color.count(2) > 1:
        return 2
    # 對子
    if 2 in color:
        return 1
    return 0


a = sys.stdin.read()
a = a.split('\n')
for x in range(int(a[0])):
    print(fun(a[x + 1]))