# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().lstrip().split()))
    arr.sort()
    count = 0
    rep=1
    for i in range(n-1):
        if arr[i]*arr[i+1]>arr[i]+arr[i+1]:
            count+=(n-(i+1))*rep
            rep=1
        if arr[i]==arr[i+1] and arr[i]==2:
            rep+=1
    print(count)