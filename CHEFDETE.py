# cook your dish here
t=int(input())
a=list(map(int,input().split()))
d={}
for i in a:
    d[i]=True
for j in range(1,t+1):
    if(d.get(j)!=True):
        print(j,end=' ')