# cook your dish here
for _ in range(int(input())):
    n=int(input())
    start=[]
    end=[]
    d={}
    for i in range(n-1):
        a,b,c=input().split(" ")
        d[a]=[b,c]
        start+=[a]
        end+=[b]
    for i in start:
        if not i in end:
            k=i
            break
    c=0
    while k in d.keys():
        print(k,d[k][0],d[k][1])
        q=""
        da=""
        for i in d[k][1]:
            if i.isnumeric():
                q+=i
            else:
                da+=i
        c+=int(q)
        k=d[k][0]
    print(str(c)+da)
    
        