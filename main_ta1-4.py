import sys
a = sys.stdin.read().split(',')
a[0] = set(a[0].split())
a[1] = set(a[1].split())
b = len(a[0] & a[1])
if b > 2:
    print(10**(b-1))
else:
    print(0)

