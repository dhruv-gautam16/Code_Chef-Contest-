
n=int(input())
for i in range(n):
    l=list(map(int,input().split()))[:2]
    if l[1] in range(l[0],l[0]+201) :
        print('YES')
    else:
        print('NO')