# cook your dish here
t=int(input())
for i in range(t):
    q=list(map(int,input().split()))
    e=input()
    f='abcdefghijklmnopqrstuvwxyz'
    c=0
    for i in range(len(f)):
        if f[i] not in e:
            c+=q[i]
    print(c)
    