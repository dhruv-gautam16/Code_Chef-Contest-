# cook your dish here
t=int(input())
while(t):
    n=int(input())
    s=input()
    o=0
    z=0
    for i in s:
        if(i=='1'):
            o+= 1
        else:
            z+=1
    if(z==o):
        print(z+o)
    else:
        x=2*min(z,o)+1
        print(x)
    t-=1