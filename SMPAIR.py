# cook your dish here
for t in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    print(l[0]+l[1])