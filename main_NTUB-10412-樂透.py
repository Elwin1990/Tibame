import sys

a = sys.stdin.read()
a = a.split('\n')
a[1] = set(map(int, a[1].split(',')))
for i in range(int(a[0])):
    a[i+2] = list(map(int, a[i+2].split(',')))
    setB = set(a[i+2])
    ans = len(a[1] & setB)
    if ans == 5:
        print('0,0,5,1')
    elif ans == 4:
        print('0,4,2,0')
    elif ans == 3:
        print('3,3,0,0')
    elif ans == 2:
        print('4,0,0,0')
    else:
        print('0,0,0,0')
