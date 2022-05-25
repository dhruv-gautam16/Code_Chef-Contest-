for t in range(int(input())):
    n,k=map(int,input().split())
    a=[int(i) for i in input().split()]
    a=sorted(a)
    if(k<=n//2):
        print(abs(sum(a[:k])-sum(a[k:])))
    else:
        print(abs(sum(a[:n-k])-sum(a[n-k:])))# cook your dish here
