# cook your dish here
t= int(input())

for i in range(t):

    n = int(input())
    
    tmp = list(map(int,input().split()))
    if(min(tmp)>=0):
        print(min(tmp)**2,max(tmp)**2)
    elif(min(tmp)<0 and max(tmp)>0):
        if(abs(max(tmp))>abs(min(tmp))):
            print(min(tmp)*max(tmp),max(tmp)**2)
        else:
            print(min(tmp)*max(tmp),min(tmp)**2)
    else:
        print(max(tmp)**2,min(tmp)**2)