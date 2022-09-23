# cook your dish here
k=100001
a=[0 for i in range(k+1)]
for i in range(1,k+1,2):
    for j in range(i,k+1,i):
        a[j]+=i 
for _ in range(int(input())):
    d,b=map(int,input().split())
    c=0
    for i in range(d,b+1):
        c+=a[i]
    print(c)