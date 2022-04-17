for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    c=0
    for i in range(n-1):
        if abs(l[i]-l[i+1])>1:
            c+=1
            break
    if c==0:
        print("YES")
    else:
        print("NO")