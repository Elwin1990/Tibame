# 想法：字元的那棵樹每被結合一次，字元的霍夫曼編碼位元數就會+1，所以只要計算每個字元被結合幾次就好

import sys

a = sys.stdin.read().splitlines()

for i in range(int(a[0])):
    if len(a[i + 1]) == 1:
        print('1')
        continue
    if len(a[i + 1]) == 2:
        print('1,1')
        continue
    a[i + 1] = a[i + 1].split(',')

    # tree[第幾個字元] = 在第幾棵樹(樹由左往右數)
    tree = [x for x in range(len(a[i + 1]))]

    # weight[第幾棵樹] = 此樹的根權重值
    weight = [int(x) for x in a[i + 1]]

    # combine: 每個字元的被結合次數(即最終的編碼位元數)
    combine = [0 for x in tree]
    weight_total = sum(weight)

    # 不管關鍵值大小了
    for k in range(len(tree) - 1):
        weight_sort = sorted(weight)
        # index0: 最小鍵值在哪棵樹
        # index1: 第二小的鍵值的樹
        index0 = weight.index(weight_sort[0])

        # 除錯: 最小的兩個鍵值相等時，會找到同一棵樹
        if weight_sort[0] == weight_sort[1]:
            index1 = weight[index0 + 1:].index(weight_sort[1]) + index0 + 1
        else:
            index1 = weight.index(weight_sort[1])

        if index0 > index1:
            index0, index1 = index1, index0

        # 被結合的兩棵樹鍵值相加後覆蓋到左邊的那棵，又變得樹鍵值直接訂為所有鍵值之總和+1，以代表此樹不存在
        for j in range(len(tree)):
            if tree[j] == index1:
                tree[j] = index0
            if tree[j] == index0:
                combine[j] += 1
        weight[index0] += weight[index1]
        weight[index1] = weight_total + 1

    combine = [str(x) for x in combine]
    print(','.join(combine))
