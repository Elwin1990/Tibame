import sys
a = sys.stdin.read().splitlines()

# 分割函數
def split(str):
    num_list = []
    num = []
    for i in str:
        if ord(i) > 47 and ord(i) < 58:
            num.append(int(i))
        else:
            if num != []:
                num_list.append(num)
            num = []
    if num != []:
        num_list.append(num)
    return num_list

# 第一個數比第二個小輸出'T'，否則輸出'F'
def small(lst1, lst2):
    for i in range(len(lst1)):
        if lst1[i] < lst2[i]:
            return 'T'
        elif lst1[i] > lst2[i]:
            return 'F'

for i in range(int(a[0])):
    data = split(a[i + 1])
    # order: list(各數字為第幾小)
    order = [0 for i in range(len(data))]
    # lengh: list(各數字的位數)
    lengh = [len(x) for x in data]
    # now: 現在正在排第幾小的數字
    now = 1
    # j: 數字為幾位數
    for j in range(1, 65):
        # count : 有幾個J位數的數字
        count = lengh.count(j)
        if count == 1:
            order[lengh.index(j)] = now
            now += 1
        elif count > 1:
            # mark: list(位數為j位的所有數字的編號)
            mark = []
            for k in range(len(lengh)):
                if lengh[k] == j:
                    mark.append(k)
            
            if count == 2:
                if small(data[mark[0]], data[mark[1]]) == 'T':
                    order[mark[0]] = now
                    now += 1
                    order[mark[1]] = now
                    now += 1
                else:
                    order[mark[1]] = now
                    now += 1
                    order[mark[0]] = now
                    now += 1
            # 對mark依照data[mark]排序，用冒泡排序法
            else:
                for x in range(len(mark) - 1):
                    for y in range(len(mark) - x - 1):
                        if small(data[mark[y]], data[mark[y + 1]]) == 'F':
                            mark[y], mark[y + 1] = mark[y + 1], mark[y]
                for x in range(len(mark)):
                    order[mark[x]] = now
                    now += 1
    order = [str(x) for x in order]
    print(', '.join(order))
