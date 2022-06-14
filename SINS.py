# cook your dish here
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)
    
    
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    print(gcd(x, y)*2)