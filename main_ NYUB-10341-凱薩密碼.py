import sys

def mi48(n):
    return n-48

def fun(n):
    num = 0
    i = 0
    ten = 1
    while i < len(n):
        if n[i] == 1:
            if ten == 1:
                num += 20
            else:
                num += 2
            i += 1
        else:
            if n[i+1] == 1:
                if ten == 1:
                    num += 10
                else:
                    num += 1
            i += 2
            ten = 0
    return num


a = sys.stdin.read()
a = a.split('\n')
for x in range(int(a[0])):
    y = fun(list(map(int ,list(a[x+1]))))
    if y < 24:
        print(chr(y+67))
    else:
        print(chr(y+41))
