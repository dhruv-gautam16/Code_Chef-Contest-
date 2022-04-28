t = int(input())
for i in range(t):
    arr = list(map(int,input().split()))
    total = 1 << 4
    res = []
    flag = False
    for i in range(1,total):
        for j in range(4):
            temp = 1 << j
            if i & temp:
                res.append(arr[j])
        if sum(res) == 0:
            flag = True
            break
        res = []
    if flag:
        print("Yes")
    else:
        print("No")