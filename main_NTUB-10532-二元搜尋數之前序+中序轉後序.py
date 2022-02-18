import sys
a = sys.stdin.read().splitlines()

def fun(lst, n):
    check = 0
    for i in range(len(lst)):
        if check == 0:
            if n in lst[i]:
                check = 1
                if len(lst[i]) == 1:
                    yield lst[i]
                    continue
                else:
                    index = lst[i].index(n)
                    if index == 0 or index + 1 == len(lst[i]):
                        del lst[i][index]
                        yield lst[i]
                        yield [n]
                        continue
                    else:
                        del lst[i][index]
                        yield lst[i][:index]
                        yield lst[i][index:]
                        yield [n]
                        continue
            else:
                yield lst[i]
        else:
            yield lst[i]

for i in range(int(a[0])):
    inorder = [[int(x) for x in a[2 * i + 1].split(',')]]
    preorder = [int(x) for x in a[2 * i + 2].split(',')]
    postorder = inorder
    for j in preorder:
        postorder = list(fun(postorder, j))
    ans = [str(i[0]) for i in postorder]
    print(','.join(ans))
