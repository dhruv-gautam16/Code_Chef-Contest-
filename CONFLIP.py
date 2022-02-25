t=int(input())
for _ in range(t):
    g=int(input())
    for e in range(g):
        i,n,q=map(int,input().split())
        if(i==1):
            if(n%2==1):
                if(q==1):
                    print(n//2)
                else:
                    print((n//2)+1)
            else:
                print(n//2)
        else:
            if(n%2==1):
                if(q==1):
                    print((n//2)+1)
                else:
                    print(n//2)
            else:
                print(n//2)