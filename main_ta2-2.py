import sys
a = sys.stdin.read().split()
str1 = ''
i=0
while i < len(a):
    str1 += str(int(a[i]) + 1) + ' '
    i += 1
print(str1.strip())