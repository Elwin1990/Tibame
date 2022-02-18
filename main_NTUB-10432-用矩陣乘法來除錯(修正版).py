import sys

a = sys.stdin.read()
a = a.split('\n')
row = 1
for i in range(int(a[0])):
    a[row] = list(map(int, a[row].split(',')))
    for j in range(1, 2 * a[row][0] + a[row][2] + 1):
        a[row + j] = list(map(int, a[row + j].split()))
    row_A, row_B, row_AB = row + 1, row + a[row][0] + 1, row + a[row][0] + a[
        row][2] + 1

    for j in range(2 * a[row][0] + a[row][2]):
        if 9999 in a[row_A + j]:
            x = j
            y = a[row_A + j].index(9999)
            a[row_A + j][y] = 0
            break
    if x < a[row][0]:
        # 找出 A_x,y * B_y,k 中使 B_y,k 不為 0 之 k
        for j in range(a[row][2]):
            if a[row_B + j][y] != 0:
                k = j
        sum = 0
        for j in range(a[row][2]):
            sum += a[row_A + x][j] * a[row_B + j][y]
        print((a[row_AB + x][y] - sum) // a[row_B + k][y])
    # 9999 在 B 的case
    else:
        x -= a[row][0]
        for j in range(a[row][2]):
            if a[row_A + j][x] != 0:
                k = j
        sum = 0
        for j in range(a[row][2]):
            sum += a[row_A + k][j] * a[row_B + j][y]
        print((a[row_AB + k][y] - sum) // a[row_A + k][x])

    row += 2 * a[row][0] + a[row][2] + 1
