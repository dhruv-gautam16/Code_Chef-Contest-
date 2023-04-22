
for _ in range(int(input())):
    n,x = map(int,input().split())
    print("YES") if x%n==0 else print("NO")