# cook your dish here
t=int(input())
while(t!=0):
    n=int(input())
    a=list(map(int,input().split(' ')))
    p,neg,c=0,0,0
    '''
    indices=[]
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if((a[i]*a[j]) > 0):
                indices.append([i+1,j+1])
                #spli
    print(len(indices))
    #print(*indices)
    '''
    for i in a:
        if(i>0):
            p+=1
        elif(i<0):
            neg+=1
            
    if(p>0):
        c=(p*(p-1)//2)
    if(neg>0):
        c+=(neg*(neg-1)//2)
    print(c)
    t-=1