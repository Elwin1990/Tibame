import sys


def fun(str1):
    count = 1
    max = 1
    x = list(str1)
    for i in range(1, len(x)):
        if int(x[i - 1]) <= int(x[i]):
            count += 1
            if count > max:
                max = count
        else:
            count = 1
    print(max)

a = sys.stdin.read()
a = a.split('\n')
lengh = len(a)
for x in a:
    fun(x)

