for _ in range(int(input())):
    n = int(input())
    num = 0
    while num<n:
        if not num%2:
            for i in range(num*n,num*n+n):
                print(i+1, end=' ')
        else:
            for i in range(num*n+n,num*n,-1):
                print(i, end=' ')
        print()
        num+=1