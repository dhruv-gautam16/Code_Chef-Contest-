# cook your dish here
for _ in range(int(input())):
    n,m=map(int,input().split())
    my={}
    for i in range(n):
        d,v=map(int,input().split())
        if d in my.keys():
            if(my[d]<v):
                my[d]=v
        else:
            my[d]=v
            
    m1=0
    m2=0
    for i in my.keys():
        if(my[i]>m1 and my[i]>m2):
            m2=m1
            m1=my[i]
        else:
            if(my[i]>m2):
                m2=my[i]
    print(m1+m2)