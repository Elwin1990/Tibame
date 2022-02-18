import sys
dic = {'-----':0, '.----':1, '..---':2, '...--':3, '....-':4, '.....':5, '-....':6, '--...':7, '---..':8, '----.':9}
a = sys.stdin.read().splitlines()
for i in range(int(a[0])):
    data = a[i + 1].split()
    for j in data:
        print(dic[j], end='')
    print()