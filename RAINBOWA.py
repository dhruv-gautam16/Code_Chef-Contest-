# cook your dish here
# cook your dish here
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    a1 = 0
    a2 = n-1
    flag = 1
    if arr[a1] != 1:
        flag = 0
    else:
        while a1 < a2:
            if arr[a1] != arr[a2]:
                flag = 0
                break
            elif (arr[a1] != arr[a1+1]) and (arr[a1]+1 != arr[a1+1]):
                flag = 0
                break
            a1 += 1
            a2 -= 1
        if arr[a1] != 7:
            flag = 0
    if flag:
        print('yes')
    else:
        print('no')