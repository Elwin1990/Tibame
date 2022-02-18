import sys
a = sys.stdin.read()
if '+' in a:
    a = a.split('+')
    print(int(a[0]) + int(a[1]))
elif '-' in a:
    a = a.split('-')
    print(int(a[0]) - int(a[1]))
elif '*' in a:
    a = a.split('*')
    print(int(a[0]) * int(a[1]))
elif '/' in a:
    a = a.split('/')
    print(int(a[0]) // int(a[1]))