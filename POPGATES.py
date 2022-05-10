# cook your dish here
t=int(input())
for j in range(t):
    n,k=map(int,input().split())
    c=list(map(str,input().split()))
    for i in range(k):
        s=c.pop()
        if(s=='H'):
            for l in range(len(c)):
                if(c[l]=='H'):
                    c[l]='T'
                else:
                    c[l]='H'
    print(c.count('H'))