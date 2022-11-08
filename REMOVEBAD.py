# cook your dish here
from statistics import mode
for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    k=mode(a)
    count=0
    for i in a:
        if i!=k:
            count+=1
    print(count)
            