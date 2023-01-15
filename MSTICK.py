# cook your dish here
import math
n = int(input())
arr=[int(x) for x in input().split()]
k = int(math.log2(n))

#max table
sp = [[0 for i in range(k+1)] for j in range(n)]

for j in range(k+1):
    i=0
    while i+(1<<j)-1<n:
        if j==0:
            sp[i][j]=arr[i]
        else:
            sp[i][j] = max(sp[i][j-1],sp[i+(1<<(j-1))][j-1])
        i+=1

#min table
sp1 = [[0 for i in range(k+1)] for j in range(n)]

for j in range(k+1):
    i=0
    while i+(1<<j)-1<n:
        if j==0:
            sp1[i][j]=arr[i]
        else:
            sp1[i][j] = min(sp1[i][j-1],sp1[i+(1<<(j-1))][j-1])
        i+=1
        
def query1(l,r):
    k = r-l+1
    msb = int(math.log2(k))
    return max(sp[l][msb],sp[r-(1<<msb)+1][msb])

def query(l,r):
    k = r-l+1
    msb = int(math.log2(k))
    ans = min(sp1[l][msb],sp1[r-(1<<msb)+1][msb]) 
    m = ans+(query1(l,r)-ans)/2
    if l-1>=0:
        m = max(m,ans+query1(0,l-1))
    if r+1<=n-1:
        m = max(m,ans+query1(r+1,n-1))
    return float(m)
        
    
q = int(input())
for i in range(q):
    l,r = map(int,input().split())
    print(query(l,r))