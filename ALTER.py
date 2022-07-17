for _ in range(int(input())):
    a,b,p,q=map(int,input().split())
    if p%a!=0 or q%b!=0:
        print("NO")
        continue
    x=p/a
    y=q/b
    if abs(x-y)==1 or abs(x-y)==0:
        print("YES")
    else:
        print("NO")