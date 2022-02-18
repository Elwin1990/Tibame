prime = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79
]

import sys

a = sys.stdin.read().splitlines()

for i in range(int(a[0])):
    b = ''
    c = []
    for k in a[i + 1]:
        if ord(k) > 47 and ord(k) < 58:
            b += k
        else:
            if b == '' or b == ' ':
                b = ''
                continue
            c.append(b)
            b = ''
    if b != '' and b != ' ':
        c.append(b)
    
    data = []
    for k in range(len(c) // 2):
        data.append([c[2*k], c[2*k+1]])
    # nodes: 為一字典紀錄 {原節點編號:對應節點數值}
    nodes = dict()
    # sides: 為一列表記錄所有樹，每棵樹含有哪些邊；邊:連接的兩點的乘積
    sides = []
    now = 0
    # trees: 為一列表記錄每棵樹，每棵樹都是此樹所有點的值的乘積
    trees = []
    for j in range(len(data)):
        # 建立 nodes
        # data[j] = data[j].split(',')
        if data[j][0] not in nodes:
            nodes[data[j][0]] = prime[now]
            now += 1
        if data[j][1] not in nodes:
            nodes[data[j][1]] = prime[now]
            now += 1

        # 建立 trees 跟 sides
        if len(trees) == 0:
            sides = [[nodes[data[j][0]] * nodes[data[j][1]]]]
            trees.append(sides[0][0])
            continue

        # 找出現在輸入的邊的兩點分別在哪兩棵樹
        tree0 = -1
        tree1 = -1
        for k in range(len(trees)):
            if trees[k] % nodes[data[j][0]] == 0:
                tree0 = k
            if trees[k] % nodes[data[j][1]] == 0:
                tree1 = k

        # 如果都不在任一棵，則 trees 跟 sides 都建立新樹
        if tree0 + tree1 == -2:
            trees.append(nodes[data[j][0]] * nodes[data[j][1]])
            sides.append([nodes[data[j][0]] * nodes[data[j][1]]])

        # 如果第一個點不在任一樹，則 trees 把第一個點接到第二個點的樹；
        # 而 sides 把邊加到第二個點的樹上
        elif tree0 == -1:
            trees[tree1] *= nodes[data[j][0]]
            sides[tree1].append(nodes[data[j][0]] * nodes[data[j][1]])

        # 如果第二個點不在任一樹，則把第二個點接到第一個點的樹
        # 而 sides 把邊加到第一個點的樹上
        elif tree1 == -1:
            trees[tree0] *= nodes[data[j][1]]
            sides[tree0].append(nodes[data[j][0]] * nodes[data[j][1]])

        # 如果兩點在同一棵樹，則 trees 不做事；sides 加入此邊
        elif tree0 == tree1:
            sides[tree0].append(nodes[data[j][0]] * nodes[data[j][1]])

        # 如果兩點在不同棵樹，則把第二個點的樹整棵加到第一個點的樹
        # sides 也是且還要再加上此邊
        else:
            trees[tree0] *= trees[tree1]
            del trees[tree1]
            sides[tree0] += sides[tree1]
            sides[tree0].append(nodes[data[j][0]] * nodes[data[j][1]])
            del sides[tree1]


    # 判斷是否有迴路
    # 想法: 把此樹所有只有一個邊的點(葉子、只有一個子樹的根)刪除，重複此動作直到所有點都不只一個邊
    cycle_exit = 0
    for j in range(len(trees)):
        # sigma: 所有邊的乘積
        sigma = 1
        for k in sides[j]:
            sigma *= k

        # check: 判斷是否已移除所有一個邊的點：0 為還沒找完；1為找完
        check = 0
        while check == 0:
            check = 1

            # node_del: 記錄此輪要刪掉的所有點
            node_del = []
            for m in nodes:
                # node_in: 收集所有此點所連結的邊
                node_in = []
                for n in range(len(sides[j])):
                    if sides[j][n] % nodes[m] == 0:
                        node_in.append(n)
                # 如果連接的邊只有一個，則刪掉此邊
                if len(node_in) == 1:
                    sigma //= sides[j][node_in[0]]
                    del sides[j][node_in[0]]
                    node_del.append(m)
                    check = 0
        
        if len(sides[j]) > 0:
            cycle_exit = 1
            # cycle: 此迴路有的點的數值(即nodes[點]))
            cycle = []
            for m in sides[j]:
                for n in nodes:
                    if m % nodes[n] == 0:
                        if n not in cycle:
                            cycle.append(n)

    if cycle_exit == 1:
        cycle = [int(x) for x in cycle]
        cycle.sort()
        print(', '.join([str(x) for x in cycle]))


    elif len(nodes) - 1 == len(data):
        print('T')

    else:
        print('F')
