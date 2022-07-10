# cook your dish 
from math import*
t=int(input())
for j in range(t):
    n=int(input())
    count=0
    for i in range(1,int(sqrt(n))+1):
        if(n%i==0):
            if(n//i==i):
                b=str(i)
                if('4' in b or '7' in b):
                    count+=1
            else:
                c=str(n//i)
                if('4' in c or '7' in c):
                    count+=1
                d=str(i)
                if('4' in d or '7' in d):
                    count+=1
    print(count)
                