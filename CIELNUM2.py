n=int(input())
count1=0
for _ in range(n):
    arr=list(input().split())
    price=int(arr[-1])
    c=0
    l=[]
    price
    while price>0:
        a=price%10
        c=c+1
        if(a==3 or a==5 or a==8):
            l.append(a)
        else:
                break
        price=int(price/10)
    if(c==len(l) and l.count(8)>=l.count(5) and l.count(5)>=l.count(3)):
        count1=count1+1
print(count1)   