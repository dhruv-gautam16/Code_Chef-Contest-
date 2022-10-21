# cook your dish here
t=int(input())
for i in range(t):
    n,b=map(int, input().split())
    l=[]
    for i in range(n):
        temp=list(map(int, input().split()))
        l.append(temp)
    m =0
    for i in l:
        if(i[0]*i[1] > m and i[-1] <= b):
            m=i[0]*i[1]
    if(m > 0):
        print(m)
    else:
        print('no tablet')
        