# cook your dish here
T=int(input())
for t in range(T):
    n=int(input())
    S=str(input())
    P=str(input())
    c0=0 
    c1=0 
    for p in P:
        if p=='0':
            c0+=1 
        else :
            c1+=1 
    if min(c1,c0)>=1:
        print('YES')
    else :
        if S==P:
            print('YES')
        else :
            print('NO')