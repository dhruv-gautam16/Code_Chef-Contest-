for _ in range(int(input())):
    n=int(input())
    s=input()
    l=[]
    for i in s:
        if s.count(i)%2==0:
            l.append("1")
        else:
            l.append("0")
    if "0" not in l:
        print("YES")
    else:
        print("NO")