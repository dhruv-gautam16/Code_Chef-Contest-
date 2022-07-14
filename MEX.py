# cook your dish here
t=int(input())
for i in range(t):
    n,k=[int(x) for x in input().split()]
    s=[int(x) for x in input().split()]
    a=[0]*(max(s)+1)
    for i in s:
        a[i]+=1
    k1=0
    for j in range(len(a)):
        if(a[j]==0):
            k1+=1
            if(k1>k):
                print(j)
                break
    if(k1<=k):
        print(len(a)+k-k1)