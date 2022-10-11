# cook your dish here
import math
t=int(input())
for _ in range(t):
    a,b,n=map(int,input().split())
    if a%b==0:
        print(-1)
    else:
        while(1):
            if n%b!=0 and n%a==0:
                print(n)
                break
            else:
                n=n+(a-(n%a))