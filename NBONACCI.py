# cook your dish here
n,c = list(map(int,input().split()))
s = [0]*(n+1)
kp = list(map(int,input().split()))
for i in range(1,n+1):
    s[i] = s[i-1] ^ kp[i-1]
for _ in range(c):
    k = int(input())
    print(s[k % (n+1)])
    
    