t=int(input())
for i in range(t):
    Pa,Pb,Qa,Qb=map(int,input().split())
    if Pa>Pb:
        r=Pa
    else:
        r=Pb
    if Qa>Qb:
        q=Qa
    else:
        q=Qb
    if r>q:
        print("Q")
    elif r==q :
        print("TIE")
    else:
        print("P")