t = int(input())
for i in range(t):
    n,m,q = map(int,input().split())
    # N=number of people, M=Seats, Q=Number of Queries
    peopleArray = [0]*n
    flag = 0
    count = 0
    for j in range(q):
        s = input().split()
        f = int(s[1])
        if s[0]=='-':
            f = (-1)*f
            peopleArray[abs(f)-1]-=1
            count-=1
        else:
            peopleArray[f-1]+=1
            count += 1
        if count>m or count<0:
            flag=1
        if peopleArray[abs(f)-1]<0 or peopleArray[abs(f)-1]>1:
            flag =1;
    if flag == 0:
        print('Consistent')
    else:
        print('Inconsistent')
        
    
