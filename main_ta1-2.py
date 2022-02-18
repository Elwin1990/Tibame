import sys
# method 1
# str1 = sys.stdin.read()
# str2 = str1.split()
# i = int(str2[0])
# print(str2[i])



str1 = sys.stdin.read().split()
print(f'{str1[int(str1[0])]}')