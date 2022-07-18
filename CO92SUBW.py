# cook your dish here
for _ in range(int(input())):
    n = int(input())
    k = ((1+8*n)**0.5)-1
    k = int(k//2)
    p = (k*(k+1))//2
    q = ((k+1)*(k+2))//2
    print(min(n-p+k,q-n+k+1))