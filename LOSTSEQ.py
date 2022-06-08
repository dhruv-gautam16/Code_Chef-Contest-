# cook your dish here
t = int(input())
while t:
    n = int(input())
    b = [int(i) for i in input().split()]
    ans = sum(b)
    print("YES") if ans%2==0 else print("NO")
    t-=1