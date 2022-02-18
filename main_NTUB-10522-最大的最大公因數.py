import sys

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
    x = []
    for j in range( len(a[i+1]) - 1 ):
        for k in range(j + 1, len(a[i+1])):
            x.append(gcd(int(a[i+1][j]), int(a[i+1][k])))

    print(max(x))