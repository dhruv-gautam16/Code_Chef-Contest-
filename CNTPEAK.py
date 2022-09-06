# cook your dish here
for _ in range(int(input())):
    n=int(input())
    if n<3:
        print(0)
    else:
        a=3**(n-3)
        b=n-2
        ans=10*b*a
        print(ans)
   
