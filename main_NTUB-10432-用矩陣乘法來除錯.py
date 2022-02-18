import sys


def fun(a, b):
    A = []
    B = []
    AB = []
    row = 0
    error_A = 0
    error_B = 0
    # 設置A矩陣
    for i in range(a[0]):
        A.append(list(map(int, b[row].split())))
        # 找出錯誤(9999)位置
        if 9999 in A[i]:
            error_x = i
            error_y = A[i].index(9999)
            error_A = 1
            A[error_x][error_y] = 0
        row += 1
    # 設置B矩陣
    for i in range(a[2]):
        B.append(list(map(int, b[row].split())))
        # 找出錯誤(9999)位置
        if 9999 in B[i]:
            error_x = i
            error_y = B[i].index(9999)
            error_B = 1
            B[error_x][error_y] = 0
        row += 1
        # 設置C矩陣
    for i in range(a[0]):
        AB.append(list(map(int, b[row].split())))
        row += 1
    if error_A == 1:
        sum = 0
        for j in range(a[3]):
            # 除錯:B元素有0
            if B[error_y][j] == 0:
                continue
            for i in range(a[1]):
                sum += A[error_x][i]*B[i][j]
            return (AB[error_x][j] - sum) // B[error_y][j]
    else:
        sum = 0
        for j in range(a[0]):
            # 除錯:A元素有0
            if A[j][error_x] == 0:
                continue
            for i in range(a[1]):
                sum += A[j][i]*B[i][error_y]
            return (AB[j][error_y] - sum) // A[j][error_x]
    
a = sys.stdin.read()
a = a.split('\n')
a[0] = int(a[0])
now = 1
for i in range(a[0]):
    a[now] = list(map(int, a[now].split(',')))
    print(fun(a[now], a[now + 1:now + 1 + 2 * a[now][0] + a[now][2]]))

    now += 1 + 2 * a[now][0] + a[now][2]