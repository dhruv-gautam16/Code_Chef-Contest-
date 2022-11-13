# cook your dish here
import math
t=int(input())
while(t):
    c=0
    n=int(input())
    while(n!=0):
        p=int(math.sqrt(n))
        n-=p*p 
        c+=1
    print(c)
    t-=1