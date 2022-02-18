import sys

a = sys.stdin.read().splitlines()

for i in range(int(a[0])):
    data = [int(x) for x in list(a[i + 1])]
    sum = 0
    for j, num in enumerate(data):
        if j % 2 == 0:
            if num * 2 > 9:
                sum += num * 2 - 9
            else:
                sum += num * 2
        else:
            sum += num
    if sum % 10 == 0:
        print('T')
    else:
        print('F')