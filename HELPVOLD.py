n=int(input())
lis=list(map(int,input().split()))
sum=0
lis.sort()
for i in range(len(lis)-1):
    sum+=(lis[i]*lis[i+1])
print(sum)
