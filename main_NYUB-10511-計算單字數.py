import sys
a = sys.stdin.read().splitlines()
for i in range(int(a[0])):
    k = a[i+1].split()
    print(len(k))