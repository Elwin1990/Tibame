import sys
a = sys.stdin.read().split()
x, y = int(a[0]), int(a[1])
i = 1
while i <= x:
    j = 1
    while j <= y:
        print(f'{i}x{j}={i*j}')
        j += 1
    i += 1