# cook your dish here
def prime(n):
    if n<=1:
        return False
    elif n==2:
        return True
    elif n>2 and n%2==0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False
    return True
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    for i in range(a,b+1):
        if prime(i):
            print(i)
        print()
   
    