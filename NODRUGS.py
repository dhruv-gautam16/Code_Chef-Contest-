# cook your dish here
t=int(input())
for tc in range(t):
    n,k,l=map(int,input().split())
    s=list(map(int,input().split()))
    if  s[n-1]==max(s):
        print("YES")
    else:
        if s[n-1]+k*(l-1)>max(s):
            print("Yes")
        else:
            print("No")