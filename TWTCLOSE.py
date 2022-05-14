t,n=map(int,input().split())
ar=[]
for i in range(n):
    x=input()
    if x=='CLOSEALL':
        ar.clear()
        ar=[]
    else:
        x=x.split(' ')
        y=x[1]
        if y in ar:
            ar.remove(y)
        else:
            ar.append(y)
    print(len(ar))
