# cook your dish here
poit = int(input())
for i in range(poit):
    nptel,twv = map(int, input().split(' '))
    a = list(map(int, input().split(' ')))
    h = sorted(a)
    i = nptel-1
    val = c = 0
    if sum(h) <twv:
        print(-1)
    else:
        while i >=0:
            if val >= twv:
                break
            else:
                val = val+ h[i]
                c = c+1 
                i-=1
        print(c)