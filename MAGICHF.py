# cook your dish here
# cook your dish here
for i in range(int(input())):
    n,x,s=map(int,input().split(' '))
    for i in range(s):
        a,b=map(int,input().split(' '))
        if a==x:
            x=b 
            
        elif b==x:
            x=a
        else:
            pass
    print(x)
