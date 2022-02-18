import sys
a = sys.stdin.read().splitlines()

for i in range(int(a[0])):
    data = a[i+1].split()
    # dis: 依照輸入順序紀錄邊長
    dis = []
    # side: 依照輸入順序紀錄邊，內容為: [節點, 節點]]
    side = []
    # 建立 side-dis 把 side 跟 dis 做連結，列表的同一個位置代表同一個邊
    for j in data:
        j = j.split(',')
        side.append([j[0],j[1]])
        dis.append(int(j[2]))
    # 對所有邊的成本做排序
    dis_sort = sorted(dis)
    # total: 累積成本
    total = 0
    # trees: 為現在已有哪些tree了，其內容tree為一set，tree的內容為此樹有的節點
    # trees = [tree0, tree1, tree2, ...]
    # tree = {節點, 節點, ....}
    trees = []
    # 在 trees 內建立第一個邊
    p = dis.index(dis_sort[0])
    trees.append({side[p][0],side[p][1]})
    total += dis_sort[0]
    # 把此邊從原資料內刪除
    del dis_sort[0]
    del dis[p]
    del side[p]
    side_num = 1
    # 開始建立最小生成樹
    for j in dis_sort:
        p = dis.index(j)
        # build: 判斷是否要建立此邊的變數，0為不建立、1為建立
        build = 1
        # 判斷是否有迴路: 若要建立的邊的兩節點都已在此樹裡，則此邊建立後會造成迴路
        for k in trees:
            if (side[p][0] in k) and (side[p][1] in k):
                build = 0
                break
        if build == 1:
            total += j
            tree1, tree2 = -1, -1
            # 找出此邊的兩點是分別在哪兩顆樹裡
            for k in range(len(trees)):
                if side[p][0] in trees[k]:
                    tree1 = k
                    continue
                if side[p][1] in trees[k]:
                    tree2 = k
            # 若兩點都不在任一樹裡，則建立新樹
            # 若一點在某一樹裡而另一點不在任一樹裡，則此點加入某樹
            # 若兩點分別在不同樹裡，則連結兩樹變一大樹
            if tree1 < 0 :
                if tree2 < 0:
                    trees.append({side[p][0],side[p][1]})
                else:
                    trees[tree2] = trees[tree2] | {side[p][0]}
            else:
                if tree2 < 0:
                    trees[tree1] = trees[tree1] | {side[p][1]}
                else:
                    if tree1 < tree2:
                        trees[tree1] = trees[tree1] | trees[tree2]
                        del trees[tree2]
                    else:
                        trees[tree2] = trees[tree1] | trees[tree2]
                        del trees[tree1]
            side_num += 1
        del dis[p]
        del side[p]
    print(total)
