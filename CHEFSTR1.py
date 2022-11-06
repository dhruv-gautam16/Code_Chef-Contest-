# cook your dish here
for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    k=0
    for i in range(0,n-1):
        k=k+abs(l[i+1]-l[i])
    print(k-(n-1))
        