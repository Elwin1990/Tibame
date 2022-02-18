import sys

a = sys.stdin.read().splitlines()

for i in range(int(a[0])):
    data = a[i + 1].split()
    count = 0
    for j in data:
        if 's' in j or 'S' in j:
            count += 1
    print(count)
