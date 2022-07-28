# cook your dish here
n=int(input())
for x in range(n):
    q=input()
    m=int(q.split(" ")[0])
    n=int(q.split(" ")[1])
    r=int(q.split(" ")[2])
    dict1={}
    y=input()
    for x in y.split(" "):
        if x in dict1:
            dict1[x]=dict1[x]+1
        else:
            dict1[x]=1
    dict2={}
    for x in range(1,m+1):
        m=str(x)
        if m in dict1 and dict1[m]>1:
            dict2[x]=dict1[m]
    m=str(len(dict2))+" "
    for x in sorted(dict2):
        n=str(x)
        m=m+n+" "
    print(m[:-1])