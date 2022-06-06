
for _ in range(int(input())):
    r,s = input().split()
    n = sorted(r)
    m = sorted(s)
    r = sorted(set(r))
    s = sorted(set(s))
    if (r==s):
        if (n==m):
            print("YES")
        else:
            print("NO")
    else:
        print("YES")
    
