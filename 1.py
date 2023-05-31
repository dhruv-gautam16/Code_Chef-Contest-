#add your code below this
for t in range(int(input())):
    a=int(input())
    flag=2
    d1=[]
    d=list(map(int,input().split()))
    f=len(d)
    if len(d)%2==0:
        for i in range(int(f/2)):
            if flag%2==0:
                e=min(d)
                d1.append(e)
                d.remove(e)
            else:
                e=max(d)
                d1.append(e)
                d.remove(e)
            flag+=1
        flag=0
    
    else:
        for i in range(int(f+1)):
            if flag%2==0:
                e=min(d)
                d1.append(e)
                d.remove(e)
            else:
                e=max(d)
                d1.append(e)
                d.remove(e)
            flag+=1



    print(sum(d1))



            
