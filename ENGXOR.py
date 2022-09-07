# cook your dish here
t = int(input())
for _ in range(t):
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    op,zp = 0,0
    for i in a:
        curr = bin(i).count('1')
        if curr & 1:
            op+=1
        else:
            zp+=1
    query = [int(input()) for i in range(q)]
    for b in query:
        p = bin(b).count('1')
        if p & 1:
            print(op,zp)
        else:
            print(zp,op)