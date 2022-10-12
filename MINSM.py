# cook your dish here

def gcd(a,b):

    if b == 0:
        return a
    
    return gcd(b, a%b)

for _ in range(int(input())):
    n = int(input())
    
    arr = [int(j) for j in input().split()]
    
    res = arr[0]
    
    for i in range(1, n):
        res = gcd(res, arr[i])
        
    print(res*n)
    
    