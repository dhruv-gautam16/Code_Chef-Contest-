# cook your dish here
for _ in range(int(input())):
    s,v = map(int,input().split())
    ans = s/(1.5*v)
    print(round(ans,6))