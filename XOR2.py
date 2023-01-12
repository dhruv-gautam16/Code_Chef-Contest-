# cook your dish here
for _ in range(int(input())):
    n = int(input())
    L = list(map(int,input().split()))
    if n%2 != 0:
        print("yes")
    else:
        a =L[0]
        for i in range(1,n):
            a = a ^ L[i]
        if a == 0:
            print("yes")
        else:
            print("no")