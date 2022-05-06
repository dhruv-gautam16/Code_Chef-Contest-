# cook your dish here
t=int(input())
while(t>0):
    n=int(input())
    li=list(map(int,input().split()))
    p=li.count(1)
    q=li.count(0)
    if(p>=q):
        print("1")
    else:
        print("0")
    t=t-1