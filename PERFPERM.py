# cook your dish here
for _ in range(int(input())):
    #n=int(input())
    #s=input()
    n,k=map(int,input().split())
    if n==2:
        if k==1:
            print("2 1")
            continue
        else:
            print("1 2")
            continue
    if k==n-1:
        print(n,end=" ")
        for i in range(2,n):
            print(i,end=" ")
            
        print(1)
        continue
    
    for i in range(1,k+1):
        print(i,end=" ")
    for i in range(k+1,n):
        print(i+1,end=" ")
    if i!=n:
        print(k+1,end=" ")
    print()
    
        