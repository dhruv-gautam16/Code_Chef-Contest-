for _ in range(int(input())):
    x=int(input()) 
    t=0
    for i in range(1,x+1):
        t+=i
        m=[t] 
        n=t
        for l in range(i,x+i-1):
            if l<x: 
                a=n+l
            else: 
                a=n+(2*x-l-1)
            m.append(a) 
            n=a
        print(*m)