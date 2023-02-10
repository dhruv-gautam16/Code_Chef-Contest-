# cook your dish here
for _ in range(int(input())):
    n = int(input())
    if n<4:
        if n==3:
            l = ([2,1,3])
        if n==2:
            l = ([1,2])
        elif n==1:
            l = ([1])
    else:
        if n%2==0:
            l = [n//2,(n//2)+1]
        else:
            l = [(n // 2)+1, (n // 2) + 1+1]

        for i in range(2, n - 1):
            v2 = l[-1] + 1
            v1 = l[-2] - 1
            l.append(v1)
            l.append(v2)
        l = l[0:n]
    print(*l,sep=' ')