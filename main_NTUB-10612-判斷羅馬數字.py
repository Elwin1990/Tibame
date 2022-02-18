import sys

num = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

a = sys.stdin.read().splitlines()

for i in range(int(a[0])):
    data = list(a[i + 1])
    sum = num[data[0]]
    for j in range(1, len(data)):
        if num[data[j - 1]] >= num[data[j]]:
            sum += num[data[j]]
        else:
            sum = sum + num[data[j]] - 2 * num[data[j-1]]
    print(sum)