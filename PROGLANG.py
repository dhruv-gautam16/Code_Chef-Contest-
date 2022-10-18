# cook your dish here
for _ in range(int(input())):
    a,b,c,d,e,f=map(int,input().split())
    x=[c,d]
    y=[e,f]
    if(a in x and b in x):
        print(1)
    elif(a in y and b in y):
        print(2)
    else:
        print(0)
    
