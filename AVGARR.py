# cook your dish here
T = int(input())

for i in range(T):
    n,x = map(int,input().split())
    mid = n//2
    for j in range(1,mid+1):
        print(x+j, end =" ")
        print(x-j, end= " ")
    if n % 2 == 1:
        print(x, end= " ")
    print("")