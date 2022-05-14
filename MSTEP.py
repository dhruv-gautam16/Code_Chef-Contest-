# cook your dish here
t = int(input())
for x in range(t):
    n = int(input())
    s = {}
    l = []
    for i in range(n):
        l.append([int(o) for o in input().split()])
        for y in range(n):
            s[l[i][y]]=[i,y]
    c = 0
    for m in range(2,n*n+1):
        c += abs(s[m-1][0]-s[m][0])+abs(s[m-1][1]-s[m][1])
    
    print(c)