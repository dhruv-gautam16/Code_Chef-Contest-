# cook your dish here
for _ in range(int(input())):
    arr = [i for i in input().split()]
    n = int(arr[0])
    arr = arr[1:]
    flag = False
    for i in arr:
        if i != i.lower() and i != i.upper():
            flag = True
            break
        elif i == i.lower():
            for j in i:
                if j > 'm':
                    flag = True
                    break
            if flag:
                break
        else:
            for j in i:
                if j < 'N':
                    flag = True
                    break
            if flag:
                break
    if flag:
        print('NO')
    else:
        print('YES')