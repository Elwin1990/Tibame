import sys

a = sys.stdin.read()
dic = {
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
    'G': 16,
    'H': 17,
    'I': 34,
    'J': 18,
    'K': 19,
    'L': 20,
    'M': 21,
    'N': 22,
    'O': 35,
    'P': 23,
    'Q': 24,
    'R': 25,
    'S': 26,
    'T': 27,
    'U': 28,
    'V': 29,
    'W': 32,
    'X': 30,
    'Y': 31,
    'Z': 33
}
a = list(a)
a[1:10] = list(map(int, a[1:10]))
check = dic[a[0]] // 10 + (dic[a[0]] % 10) * 9
for i in range(1, 9):
    check += a[i] * (8 - i + 1)
    # print(check)
check += a[9]
if check % 10 == 0:
    print('合法')
else:
    print('不合法')
