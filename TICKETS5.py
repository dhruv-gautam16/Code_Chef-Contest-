# cook your dish here
T=int(input())
for i in range(T):
    S=input()
    a={}
    for ele in S:
        if ele not in a:
            a[ele]=1 
        else:
            a[ele]=a[ele]+1 
    c=0 
    for key in a:
        c=c+1 
    if c==2:
        print("YES")
    else:
        print("NO")