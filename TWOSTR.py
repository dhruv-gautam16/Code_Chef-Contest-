for t in range(int(input())):
    s1=list(input())
    s2=list(input())
    for i in range(len(s1)):
        if s1[i]=='?' or s2[i]=='?':
            s1[i]=s2[i]
    if s1==s2:
        print('Yes')
    else:
        print('No')
