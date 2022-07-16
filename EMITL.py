# cook your dish here
from collections import Counter
for _ in range(int(input())):
    s = list(input())
    n = len(s)
    dic = Counter(s)
    l = [('L',2),('T',2),('I',2),('M',2)]
    arr = list(dic.keys())
    if n < 9:
        print('NO')
    elif n == 9:
        flag = True
        for i in l:
            if i[0] not in arr:
                flag = False
                break
            else:
                if 2 > dic[i[0]]:
                    flag = False
                    break
        if flag:
            if 'E' not in arr:
                flag = False
            else:
                if 1 > dic['E']:
                    flag = False
        if flag:
            print('YES')
        else:
            print('NO')
    elif n > 9:
        flag = True
        for i in l:
            if i[0] not in arr:
                flag = False
                break
            else:
                if 2 > dic[i[0]]:
                    flag = False
                    break
        if flag:
            if 'E' not in arr:
                flag = False
            else:
                if 2 > dic['E']:
                    flag = False
        
        if flag:
            print('YES')
        else:
            print('NO')