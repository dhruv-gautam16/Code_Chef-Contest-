from sys import stdin,stdout 
mod=10**9+7
s=[]
s.append([2,2,1,0])

def add():
    global s
    w=(s[-1][0]*s[-1][0])+(s[-1][1]*s[-1][2])
    x=(s[-1][0]*s[-1][1])+(s[-1][1]*s[-1][3])
    y=(s[-1][2]*s[-1][0])+(s[-1][3]*s[-1][2])
    z=(s[-1][2]*s[-1][1])+(s[-1][3]*s[-1][3])
    w%=mod
    x%=mod
    y%=mod
    z%=mod
    s.append([w,x,y,z])

def multiply(i):
    global ans
    w=(ans[0]*s[i][0])+(ans[1]*s[i][2])
    x=(ans[0]*s[i][1])+(ans[1]*s[i][3])
    y=(ans[2]*s[i][0])+(ans[3]*s[i][2])
    z=(ans[2]*s[i][1])+(ans[3]*s[i][3])
    w%=mod
    x%=mod
    y%=mod
    z%=mod
    ans=[w,x,y,z]
  
def solve():
    global ans
    n=int(stdin.readline().rstrip())
    if(n==1):
        return 1
    if(n==2):
        return 3
    b=bin(n-2)
    b=b[2:]
    b=b[::-1]
    ans=[1,0,0,1]
    l=len(b)
    for i in range(l):
        if(b[i]=='1'):
            multiply(i)
    val=(ans[0]*3)+(ans[1]*1)
    return val%mod
    
for i in range(1,31):
    add()
for _ in range(int(stdin.readline().rstrip())):
    print(solve())