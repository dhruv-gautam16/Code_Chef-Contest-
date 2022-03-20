for i in range(int(input())):
    n=int(input())
    a=[int(x) for x in input().split()]
    o=0
    e=0
    o1=[]
    e1=[]
    f=0
    for i in a:
        if(i%2==0):
            e+=1
            e1.append(i)
        else:
            o+=1
            o1.append(i)
   # print(e1)
    if(o<2 or (e==0 and o%2!=0)):
        print(-1)
    elif(e==0 and o%2==0):
        print(*o1)
    else:
        #print("SDFGH")
        f=1
        x1=[]
        if(e>o):
            if(o%2==0):
                x1=e1+o1
            else:
                x1=x1+o1[0:2:]
                x1=x1+e1
                x1=x1+o1[2::]
        else:
            if(o%2==0):
                x1=e1+o1
            else:
                x1=x1+o1[0:2:]
                x1=x1+e1
                x1=x1+o1[2::]
                
    if(f==1):
        print(*x1)