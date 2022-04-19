for i in range(int(input())):
    n,k,s = map(int,input().split())
    print(int((s-(n*n))/(k-1)))