# cook your code here
for _ in range(int(input())):
    n = input()
    a = input().split()
    d ={}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    l = max(d.values())
    y = list(d.values()).count(l)
    if (y>1):
        print("NO")
    else: 
        print("YES")
        
