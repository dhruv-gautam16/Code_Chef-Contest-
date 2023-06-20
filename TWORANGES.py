t=int(input())
for _ in range(t):
    a,b,c,d=map(int, input ().split())
    x=[]
    for i in range(a,b+1):
        x.append(i)
    for j in range(c,d+1):
        x.append(j)
    print (len(set(x)))