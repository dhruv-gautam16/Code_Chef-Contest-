# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    A=list(map(int,input().split()))
    temp=[]
    for i in range(n-1):
        if A[i]!=A[i+1]:
            temp.append(i)
            temp.append(i+1)
    result=set(temp)
    print(len(result))