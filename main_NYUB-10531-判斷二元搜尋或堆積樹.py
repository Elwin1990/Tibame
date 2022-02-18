import sys

a = sys.stdin.read()
a = a.split('\n')
for i in range(int(a[0])):
    data = [int(x) for x in a[i + 1].split(',')]

    # 判斷最小堆積樹
    check = 1
    for j in range(len(data)):
        if 2 * j + 1 < len(data):
            if data[j] > data[2 * j + 1]:
                check = 0
                break
        if 2 * j + 2 < len(data):
            if data[j] > data[2 * j + 2]:
                check = 0
                break
    if check == 1:
        print('H')
        continue

    # 判斷最大堆積樹
    check = 1
    for j in range(len(data)):
        if 2 * j + 1 < len(data):
            if data[j] < data[2 * j + 1]:
                check = 0
                break
        if 2 * j + 2 < len(data):
            if data[j] < data[2 * j + 2]:
                check = 0
                break
    if check == 1:
        print('H')
        continue

    # 判斷二元搜尋樹
    check = 1
    for j in range(len(data)):
        k = j + 1
        while k > 1:
            if k % 2 == 0:
                if data[j] > data[k // 2 - 1]:
                    check = 0
                    break
                else:
                    k = k // 2
                    continue
            else:
                if data[j] < data[k // 2 - 1]:
                    check = 0
                    break
                else:
                    k = k // 2
    if check == 1:
        print('B')
        continue

    print('F')
