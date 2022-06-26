
for i in range(int(input())):
    k=int(input())
    l1=list(map(int,input().split()))
    s=sum(l1)
    for t in range(0,k):
        print((s//(k-1))-l1[t],end=" ")
    print()
