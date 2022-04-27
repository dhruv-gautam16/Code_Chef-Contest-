# cook your dish here
t=int(input())
for _ in range(t):
    n,o=map(str, input().split())
    c=0
    for i in range(int(n)):
        a=list(map(str, input().split()))
        if a[0]=='CONTEST_WON':
            if int(a[1])<=20:
                c+=300+(20-int(a[1]))
            else:
                c+=300
        elif a[0]=='TOP_CONTRIBUTOR':
            c+=300
        elif a[0]=='BUG_FOUND':
            c+=int(a[1])
        else:
            c+=50
    if o=='INDIAN':
        print(int(c/200))
    else:
        print(int(c/400))