# cook your dish here
t=int(input())
for t in range(t):
    a,b,c=map(int,input().split())
    print(max(a,b,c)-min(a,b,c))