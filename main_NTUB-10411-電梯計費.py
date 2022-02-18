import sys

a = sys.stdin.read()
a = a.split('\n')
for i in range(int(a[0])):
    a[2 * i + 2] = list(map(int, a[2 * i + 2].split(',')))
    price = 0
    for j in range(int(a[2 * i + 1]) - 1):
        if a[2 * i + 2][j] < a[2 * i + 2][j + 1]:
            price += 20 * (a[2 * i + 2][j + 1] - a[2 * i + 2][j])
        else:
            price += 10 * (a[2 * i + 2][j] - a[2 * i + 2][j + 1])
    print(price)
