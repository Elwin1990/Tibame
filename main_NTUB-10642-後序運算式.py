cal = {'+':43, '-':45, '*':42, '/':47}
# 數字:0~9:48~57
import sys
a = sys.stdin.read().splitlines()

for t in range(int(a[0])):
    lst = []
    data = a[t + 1].split()
    for i in data:
        if i[0] in cal:
            y = lst.pop()
            x = lst.pop()
            if i == '+':
                lst.append(x+y)
            elif i == '-':
                lst.append(x-y)
            elif i == '*':
                lst.append(x*y)
            elif i == '/':
                lst.append(x//y)
        else:
            lst.append(int(i))
    print(lst[0])
