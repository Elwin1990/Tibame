import sys
a = int(sys.stdin.read())
if a % 4 != 0:
    print(False)
elif a % 100 != 0:
    print(True)
elif a % 400 != 0:
    print(False)
else:
    print(True)