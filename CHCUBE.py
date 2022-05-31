# cook your dish here
ujju=int(input())
for sai in range(ujju):
    u1=list(map(str, input().split()))
    h=max(set(u1),key=u1.count)
    g=u1.count(h)
    if((u1[0]==h or u1[1]==h) and (u1[2]==h or u1[3]==h) and(u1[4]==h or u1[5]==h) and g>=3):
        print("YES")
    else:
        print("NO")