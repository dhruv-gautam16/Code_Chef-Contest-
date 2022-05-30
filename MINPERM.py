# cook your dish here
for _ in range(int(input())):
    n=int(input())
    v=[0]*n
    for i in range(0,n):
        v[i]=i+1
    for i in range(0,n-1,2):
        v[i],v[i+1]=v[i+1],v[i]
    if(n%2==1):
        v[n-1],v[n-2]=v[n-2],v[n-1]
    for i in range(0,n):
        print(v[i] ,end=" ")
    print()