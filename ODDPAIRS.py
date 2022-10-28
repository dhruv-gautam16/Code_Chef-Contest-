# cook your dish here
t=int(input())
for tc in range(t):
    n=int(input())
    if(n%2==0):
        even=n//2
        odd=n//2
    else:
        odd=(n+1)//2
        even=n//2
    print(odd*even*2)