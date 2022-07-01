# cook your dish here
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    c = 0 
    l1 = []
    m = []
    for i in range(2*n):
        if l[i]%2==0:
            c+=1
            l1.append(l[i])
    e = c 
    o = abs(2*n - c)
    if e==o:
        print(0)
    elif o>e:
        print(abs(o-e)//2) 
    else:
        for i in l1:
            c = 0 
            while (i%2==0):
                c+=1 
                i=i//2 
            m.append(c) 
        m.sort()
        k = n-o 
        print(sum(m[:k]))