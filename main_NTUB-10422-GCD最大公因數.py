import sys
import math


def gcd(a, b):
    if b > a:
        a, b = b, a
    a, b = b, a % b
    while b != 0:
        a, b = b, a % b
    return a

a = sys.stdin.read()
a = a.split('\n')
for i in range(int(a[0])):
    a[i+1] = a[i+1].split(',')
    ans = int(a[i+1][0])
    for j in range(1, len(a[i+1])):
        ans = gcd(ans, int(a[i+1][j]))
    print(ans)