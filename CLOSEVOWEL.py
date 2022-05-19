# cook your dish here
for i in range(int(input())):
    n=int(input())
    s=input()
    l1=["c","g","l","r"]
    a=1
    for j in range(n):
        if s[j] in l1:
            a=a*2%(10**9+7)
    if a==1:
        print(a%(10**9+7))
    else:
        print(a)