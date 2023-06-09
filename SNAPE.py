# cook your dish here
import math
n=int(input())
for i in range(1,n+1):
    a,b=map(int,input().split())
    c=math.pow(a,2)
    d=math.pow(b,2)
    q=c+d;
    w=abs(c-d)
    x=math.sqrt(q)
    y=math.sqrt(w)
    #print("%.5f"%float(y),round(x,4))
    print(round(y,4),round(x,4))