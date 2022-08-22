# cook your dish here
t = int(input())

for i in range(t):
    c = 0 
    n = int(input())
    l1 = list(map(int, input().split())) 
    l2 = list(map(int, input().split()))  
    d = {}
    for j in range(len(l1)):
        d[l1[j]] = [j + 1, l2[j]] 
    for k in range(2, len(l1) + 1):
        while d[k][0] <= d[k - 1][0]:
            d[k][0] += d[k][1] 
            c += 1 
    print(c)