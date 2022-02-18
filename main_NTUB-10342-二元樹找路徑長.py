import sys


def fun(a, start_roots, tree):
    r = start_roots
    dis = 0
    r = a[r][tree]
    while r < 999:
        dis += 1
        r = a[r][tree]
    return dis


# 陣列: a[row][tree]
a = sys.stdin.read()
a = a.split('\n')
total_data = int(a[0])
now_rows = 1
for x in range(1, total_data + 1):
    a[now_rows] = list(map(int, a[now_rows].split(',')))
    roots, trees, obj = a[now_rows][0], a[now_rows][1], a[now_rows][2]
    for j in range(roots):
        a[now_rows + j + 1] = list(map(int, a[now_rows + j + 1].split()))
    
    # 主行數: now_rows+1 ~ now_rows+roots+1
    for j in range(trees):
        print(fun(a[now_rows + 1:now_rows + roots + 1], obj, j + 1), end='')
        if j + 1 < trees:
            print(',', end='')
    print()
    now_rows += roots + 1
