import sys
a = int(sys.stdin.read())
i = 1
x, y = 0, 1
if a == 1 :
    print(0)
elif a == 2:
    print(1)
else:
    while i < a:
        x, y = y, x + y
        i += 1
    print(x)