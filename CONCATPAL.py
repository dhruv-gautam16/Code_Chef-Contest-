# cook your dish here
t = int(input())
for i in range(t):
    n, m = map(int, input().split(' '))
    s1 = list(input())
    s2 = list(input())
    
    cs = []
    condition = 'YES'
    
    if m>n:
        m,n = n,m
        s1, s2 = s2, s1
        
    j = 0
    
    while j < len(s2):
        if s2[j] in s1:
            cs.append(s2[j])
            s1.remove(s2[j])
            s2.pop(j)
        
        else:
            condition = 'NO'
            break
    
    oc = 0
    tot = 0
    l = len(s1)
    
    for j in 'abcdefghijklmnopqrstuvwxyz':
        c = s1.count(j)
        tot += c
        if c%2:
            oc += 1
        if l%2 and oc>1:
            condition = 'NO'
        elif l%2 == 0 and oc>0:
            condition = 'NO'
        if tot == l:
            break
        
    print(condition)
    