# cook your dish here
test=int(input())
for i in range(test):
    ans={}
    s,k=map(int,input().split())
    arr=list(map(int,input().split()))
    for j in arr:
        if j not in ans:
            ans[j]=1 
        else:
            ans[j]+=1 
    #print(ans)
    s1=0
    a=1
    for j in ans.items():
        if j[1]==k:
            a=0
            s1+=j[0]
    if a==1:
        print(-1)
    else:
        print(s1)