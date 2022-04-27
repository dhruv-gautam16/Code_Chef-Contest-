t=int(input())
for i in range(t):
    n1=int(input())
    l1=list(map(int,input().split()))
    rent=0
    fine=0
    for i in range(len(l1)):
        if l1[i]==0:
            rent+=1
        if rent!=0:
            fine+=1
    print(rent*1000+fine*100)
