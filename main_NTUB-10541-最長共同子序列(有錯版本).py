import sys

a = sys.stdin.read().splitlines()

for i in range(int(a[0])):
    if len(a[2 * i + 1]) < len(a[2 * i + 2]):
        str1 = list(a[2 * i + 1])
        str1 = list(a[2 * i + 2])
    else:
        str1 = list(a[2 * i + 2])
        str2 = list(a[2 * i + 1])
    count = 0
    for j in str1:
        if j in str2:
            count += 1
            str2.remove(j)
    print(count)
