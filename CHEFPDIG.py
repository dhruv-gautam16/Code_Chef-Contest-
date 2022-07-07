# cook your dish here
for _ in range(int(input())):
    x=list(input())
    d=' '
    for i in range(65,91):
        c=list(str(i))
        count=0
        for j in c:
            if j in x and x.count(j)>=c.count(j):
                count +=1
        if count==len(c):
            d =d+chr(i)
    print(d)