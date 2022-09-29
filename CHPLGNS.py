for _ in range(int(input())):
    n=int(input())
    arr=[]
    ans=[0]*n 
    for i in range(n):
        m=int(input())
        po=[int(i) for i in input().split()][::2]
        arr.append([i,max(po)])
    arr.sort(key=lambda x:x[1])
    for x in range(n):
        ans[arr[x][0]]=x 
    print(*ans)