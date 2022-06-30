# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=[]
    invalid=0
    for i in range(n):
        a=list(map(int,input().split()))
        l.append(a)
        if 0 not in a:
            invalid=1
    for row in range(n):
        val=0
        for col in range(n):
            if l[col][row]==0:
                val=1
        if val==0:
           invalid=1
           break
       
    if invalid==1:
        print("NO")
    else:
        print("YES")
        