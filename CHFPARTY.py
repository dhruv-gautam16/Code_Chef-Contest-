t= int(input())
while t:
    t-=1
    n=int(input())
    num=list(map(int,input().strip().split()))[:n]
    num.sort()
    k=0
    for i in num:
        if i>k:
            break
        else:
           k+=1
    print(k)