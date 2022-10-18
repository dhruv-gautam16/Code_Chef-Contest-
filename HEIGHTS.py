t=int(input())
while(t>0):
    t-=1 
    n=int(input())
    arr=list(map(int,input().strip().split()))
    maximum=max(arr)
    d=dict()
    arr2=[]
    onlytwo=True
    count=0
    for i in arr:
        if i in d:
            d[i]+=1 
        else:
            d[i]=1 
    for x,y in d.items():
        if y!=2 and x!=maximum:
            onlytwo=False 
        if y==1:
            arr2.append(x)
    # print(arr2)
    # print(d)
    if len(arr2)%2==0:
        count=len(arr2)//2 
    elif len(arr2)%2==1:
        count=len(arr2)//2+1 
    if len(arr2)==1 and arr2[0]==maximum:
        if onlytwo:
            count=2 
        else:
            count=1 
    print(count)
    
            
