# cook your dish here
mdl = 1000000
for _ in range(int(input())):
    z = input().split()
    n,a,b,c,d = map(int, z[:5])
    sqd = dict()
    sqd[d]=0
    r = d
    for e in range(1,n):
        r = ((a*r + b)*r + c)%mdl
        try:
            sqd[r] *= 1
            break
        except KeyError:
            sqd[r] = e
            
    if len(sqd)==n:
        picks = list(sqd.keys())
    else:
        inrun = list(sqd.items())
        inrun.sort(key=lambda x: x[1])
        nunq =len(sqd)
        repst = sqd[r]
        picks = [inrun[e][0] for e in range(0, repst)]
        reprun = [inrun[e][0] for e in range(repst, nunq)]
        cyc = (n-len(picks))//len(reprun)
        runout = (n-len(picks))%len(reprun)
        if 0 == cyc % 2:
            picks.extend(reprun[:runout])
        else:
            picks.extend(reprun[runout:])
            
    picks.sort(reverse=True)
    np = len(picks)
    sth = sum(picks[0:np:2]) - sum(picks[1:np:2])
    print(sth)      
    
