for _ in range(int(input())):
    N=int(input())
    arr1,arr2=[],[]
    arr=list(map(int,input().split(' ')))
    for i in range(2*N):
        if(i>=N and arr[i]<N+1):
            arr2.append(i)
        elif(i<N and arr[i]>=N+1):
            arr1.append(i)
    ans=len(arr1)
    for i in range(len(arr1)):
        ans+=arr2[i]-arr1[i]-1
    print(ans)