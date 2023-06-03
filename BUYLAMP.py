# cook your dish here
for i in range(int(input())):
    n,k,x,y = map(int,input().split())
    a = k * x
    print(a + ((n - k)*min(x,y)))