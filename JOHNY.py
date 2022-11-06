# cook your dish here
for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    k=int(input())
    s=l[k-1]
    l.sort()
    p=l.index(s)
    print(p+1)
    