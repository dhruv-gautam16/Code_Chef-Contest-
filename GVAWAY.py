# cook your dish here

T = int(input())
for t in range (T):
    l,r,k = map(int,input().split())
    if l==r:
        print(1)
    else:
        print(k)
