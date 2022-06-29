# cook your dish here
for _ in range(int(input())):
    n=int(input())
    if (n%4!=0):
        print("NO")
    else:
        print("YES")
        l=list(range(1,n+1))
        l1=[]
        l2=[]
        l1=l[:n//2:2]+l[(n//2)+1::2]
        l2=list(set(l)-set(l1))
        print(*l1)
        print(*l2)
        
