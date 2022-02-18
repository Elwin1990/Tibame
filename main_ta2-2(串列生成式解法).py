import sys
a = sys.stdin.read().split()
b =' '.join([str(int(i) + 1) for i in a])
print(b)