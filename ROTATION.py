# cook your dish here
from collections import deque
l,m=map(int,input().split())
a=list(map(int,input().split()))
a=deque(a)
for j in range(m):
    s,n=input().split( )
    if(s=='C'):
        a.rotate(-int(n))
    elif(s[0]=='A'):
        a.rotate(int(n))
    else:
        print(a[int(n)-1])
