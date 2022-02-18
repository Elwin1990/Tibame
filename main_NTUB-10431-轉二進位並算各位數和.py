import sys
import math


a = sys.stdin.read()
a = a.split('\n')
for i in range(int(a[0])):
    count = 0
    n = int(a[i+1])
    while n > 0:
        count += n % 2
        n = n //2
    print(count)
    