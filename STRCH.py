for _ in range(int(input())):
    n = int(input())
    arr,x = map(str,input().split())
    l = []
    count = 0
    ans = 0
    for i in range(n):
        if arr[i] == x:
            l.append(i)
            count += 1
            if count >= 2:
                ans += (l[count - 2] + 1)*(l[count - 1] - l[count - 2] - 1) + l[count - 2] + 1 
    if l != []:
        ans += (l[-1]+1)*(n - 1 - l[-1]) + l[-1] + 1
    print(ans)