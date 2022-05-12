# cook your dish here
for _ in range(int(input())):
    n=int(input())
    if n%2!=0:
        print(-1)
    else:
        print("1"*(n//2)+"0"*(n//2))
