lis=[]
t=int(input())
while t>0:
    n=int(input())
    lis.append(n)
    t-=1
lis.sort()
for i in range(0,len(lis)):
    print(lis[i])
