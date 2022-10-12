# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    s=str(input())
    x=s[0]
    p=1
    for i in range(1,n):
        if s[i]==x:
            break
        p+=1
    print(p)