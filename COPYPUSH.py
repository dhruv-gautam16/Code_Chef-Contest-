# cook your dish here
for _ in range(int(input())):
    n=int(input())
    s=input()
    while len(s)>0:
        if len(s)%2==1:
            s=s[:-1]
        else:
            k=len(s)//2
            if s[:k]==s[k:]:
                s=s[:k]
            else:
                break
    if len(s)==0:
        print("YES")
    else:
        print("NO")

