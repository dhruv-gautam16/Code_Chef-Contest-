# cook your dish here
t = int(input())
for _ in range(t):
    sd,ed,l,r = input().split(" ")
    l,r = int(l),int(r)
    # print(sd,ed,l,r)
    d = {'saturday':0,'sunday':1,'monday':2,'tuesday':3,'wednesday':4,
   'thursday':5,'friday':6}
    # x = abs(days[sd] - days[ed])+1
    
    if d[ed]>=d[sd]:
        x = d[ed]-d[sd]+1 
    else:
        x = d[ed]-d[sd]+8 
    temp = 0
    count = 0
    # print(x)
    while(x<=r):
        if l<=x<=r:
            temp = x
            count+=1
        x+=7
    
    if count==0:
        print('impossible')
    elif count==1:
        print(temp)
    else:
        print('many')