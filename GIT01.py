# cook your dish here
for _ in range(int(input())):
    n,m=map(int,input().split())
    c1,c2=0,0
    for i in range(n):
        l=input()
        for j in range(m):
            if (i+j)%2==0:
                if l[j]=="G":
                    c1+=3
                else:
                    c2+=5
            else:
                if l[j]=="G":
                    c2+=3
                else:
                    c1+=5
    print(min(c1,c2))