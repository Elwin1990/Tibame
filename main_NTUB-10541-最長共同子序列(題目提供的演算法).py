import sys

a = sys.stdin.read().splitlines()


for i in range(int(a[0])):
    if len(a[2 * i + 1]) < len(a[2 * i + 2]):
        str1 = list(a[2 * i + 1])
        str2 = list(a[2 * i + 2])
    else:
        str1 = list(a[2 * i + 2])
        str2 = list(a[2 * i + 1])
    
    array = [[]]
    for j in range(len(str1) + 1):
        for k in range(len(str2) + 1):
            if j == 0:
                array[0].append(0)
            elif k == 0:
                array.append([0])
            elif str1[j - 1] == str2[k - 1]:
                array[j].append(array[j-1][k-1] + 1)
            else:
                max1 = max(array[j-1][k], array[j][k-1])
                array[j].append(max1)


    print(array[j][k])
