import sys
a = sys.stdin.read().splitlines()
for i in range(int(a[0])):
    data = a[i + 1].split('/')
    x, y = data[0].split('.'), data[1].split('.')
    z = []
    for j in range(4):
        z.append(int(x[j]) | (255 - int(y[j])))   
    z = [str(k) for k in z]
    print('.'.join(z))

