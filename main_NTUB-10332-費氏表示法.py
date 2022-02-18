import sys
import math


def feb(n):
    f = [1, 1]
    a = 2
    ref = n
    while f[a-1] < n:
        f.append(f[a-2]+f[a-1])
        a += 1
    # print(f)
    lengh = len(f)
    if f[lengh-1] > n:
        f.pop()
        lengh -= 1

    for i in f[lengh-1::-1]:
        if ref >= i:
            print('1', end='')
            ref -= i
        else:
            print('0', end='')
        if i ==1:
          return print('')
    

a = sys.stdin.read()
a = a.split('\n')
for x in range(int(a[0])):
    print(a[x+1], end='=')
    feb(int(a[x+1]))