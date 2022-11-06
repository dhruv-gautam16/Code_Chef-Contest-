# cook your dish here
for i in range(int(input())):
    n=int(input())
    d={}
    for i in range(n):
        a,b=map(int,input().split())
        if(a<9):
            if a not in d:
                d[a]=b
            else:
                if d[a]<b:
                    d[a]=b
    print(sum(d.values()))
            

