for t in range(int(input())):
    n=int(input())
    one = 0
    zero = 0
    s=str(input())
    for i in range(n):
        if s[i]=='1':
            one+=1
        else:
            zero+=1
    if one==0 or zero==0:
        print(s)
    else:
        res = ''.join(sorted(s))
        print(res)


