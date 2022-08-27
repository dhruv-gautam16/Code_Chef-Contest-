# cook your dish here
T = int(input())
while T>0:
    N,K = map(int,input().split())
    arr = []
    inp = input().split()
    for i in inp:
        arr.append(i)
    x = int(0)
    for i in range(0,N):
        for j in range(i+1,N):
            if int(arr[i])>int(arr[j]):
                x=x+1
    y = int(0)            
    for i in range(0,N):
        for j in range(i+1,N):
            if int(arr[i])<int(arr[j]):
                y = y+1
    res = int((K+1)*K*x*(0.5))+int((K-1)*K*y*(0.5))
    print(res)
    T=T-1    
