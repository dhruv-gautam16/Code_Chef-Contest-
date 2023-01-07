# cook your dish here
# cook your dish here
import math
for i in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    l1 = [[]]
    for i in range(len(l) + 1):
        for j in range(i):
            l1.append(l[j: i])
    #print(l1)
    l2=[i for i in l1 if(math.prod(i)%k==0)]
    #print(l2)
    if(len(l2)>0):
        print('YES')
    else:
        print('NO')