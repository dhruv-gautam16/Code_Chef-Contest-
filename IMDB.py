# cook your dish here
a=int(input())
for i in range(a):
    (b,c)=map(int,input().split())
    l=[]
    for j in range(b):
        (d,t)=map(int,input().split())
        if d<=c:
            l.append(t)
    print(max(l))
        