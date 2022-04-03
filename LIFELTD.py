for _ in range(int(input())):
    a=[]
    c=0
    for i in range(3):
        a.append([x for x in input()])
    for i in range(3):
        for j in range(3):
            if(i!=2 and j!=2 and a[i][j]=='l' and a[i+1][j]=='l' and a[i+1][j+1]=='l'):
                print('yes')
                c=1 
                break
        if c==1:break
    else:print('no')
            
            
