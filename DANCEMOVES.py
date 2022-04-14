# cook your dish here
T=int(input())
x=[]
y=[]
for i in range(T):
    a,b=input().split()
    x.append(a)
    y.append(b)
for i in range(T):
    k=0
    c=int(x[i])
    d=int(y[i])
    while c!=d:
        if c<d:
            c=c+2
            k+= 1
        elif c>d:
            c=c-1
            k+= 1
    print(k)        

        