for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    s = []
    t = 1
    for i in range(len(l)-1):
        if 2>=l[i+1]-l[i]:
            t+=1
        elif l[i+1]-l[i]>2:
            s.append(t)
            t = 1
    s.append(t)
    print(min(s),max(s))
        