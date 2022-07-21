# cook your dish here
T = int(input())

def isPossible(n, m):
    if n == 1 or m == 1:
        if n > 2 or m > 2: return False
        
    if n%2==0 or m%2==0: return True
    else: return False
        
while T:
    T -= 1
    n, m = map(int, input().split(" "))
    if isPossible(n, m):
        print("Yes")
    else: 
        print("No")