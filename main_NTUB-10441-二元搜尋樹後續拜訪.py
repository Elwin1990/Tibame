import sys
# 樹的各節點位置為依照二元完全樹編號，根為1，每個節點的左子節點編號為節點的兩倍、右子節點的編號為兩倍加一



# 建立二元搜尋樹  dic: 已造出的樹；  x: 要加入的值
# 依照二元搜尋樹的方法，在已造出的樹中，從根開始找，若要加入的值彼此節點小，則往左子樹找；若比較大，則往右子樹找
def add_n(dic, x):
    n = 1
    while n in dic:
        if x < dic[n]:
            n = 2 * n
        else:
            n = 2 * n + 1
    return n


data = sys.stdin.read().split('\n')

for k in range(int(data[0])):
    a = int(data[2 * k + 1])
    b = [int(i) for i in data[2 * k + 2].split(',')]
    dic1 = {}  # 位置 : 值
    dic2 = {}  # 值   : 位置
    # 建立樹
    for i in range(a):
        n = add_n(dic1, b[i])
        dic1[n] = b[i]
        dic2[b[i]] = n

    # 對所有值做排序，並依序取出
    b = sorted(b)
    while len(b) > 1:
        for i in range(len(b)):
            # 若此點沒有左右子樹，則輸出
            if (2 * dic2[b[i]] not in dic1) and ((2 * dic2[b[i]] + 1) not in dic1):
                n = i
                break
        print(b[n], end=',')
        del dic1[dic2[b[n]]]
        del dic2[b[n]]
        del b[n]
    print(b[0])
