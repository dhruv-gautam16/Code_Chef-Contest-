# cook your dish here
n = int(input())
while n>0:
    n = n-1
    a = int(input())
    b = list(map(int,input().split()))
    s = int(sum(b)/(a+1))
    for i in range(a):
        print(b[i]-s,end=" ")
    print()