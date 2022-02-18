import sys
b = ['星期一', '星期二', '星期三', '星期四']
a = sys.stdin.read().split()
if a[0] in b:
    print(int(a[1]) * int(a[2]))
else:
    print('不開市')