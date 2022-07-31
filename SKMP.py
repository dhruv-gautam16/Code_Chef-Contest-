# cook your dish here
for _ in range(int(input())):
    s=input()
    p=input()
    u=[p[0]]
    for e in p[1:]:
        if e not in u:
            u.append(e)
    s=s+p[0]
    s=''.join(sorted(s))
    for e in p:
        s=s.replace(e, "", 1)
    pos=0
    if u[0]<u[1]:
        pos=s.rfind(p[0])
    else:
        pos=s.find(p[0])
    print(s[:pos]+p+s[pos+1:])