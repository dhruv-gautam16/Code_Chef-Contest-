
t = int(input())
for _ in range(t):
    l=[int(x) for x in input().split()]
    d={l[i]:l[i+3] for i in range(3)}
    e=sorted(d)
    if len(d)==1:
        if l[3]==l[4]==l[5]:
            print("FAIR")
        else:
            print("NOT FAIR")
    elif len(d)==2:
        if l[0]==l[1]:
            if l[0]>l[2]:
                if l[3]==l[4] and l[3]>l[5]:
                    print("FAIR")
                else:
                    print("NOT FAIR")
            else:
                if l[3]==l[4] and l[3]<l[5]:
                    print("FAIR")
                else:
                    print("NOT FAIR")
        elif l[1]==l[2]:
            if l[1]>l[0]:
                if l[4]==l[5] and l[4]>l[3]:
                    print("FAIR")
                else:
                    print("NOT FAIR")
            else:
                if l[4]==l[5] and l[4]<l[3]:
                    print("FAIR")
                else:
                    print("NOT FAIR")
        else:
            if l[0]>l[1]:
                if l[3]==l[5] and l[3]>l[4]:
                    print("FAIR")
                else:
                    print("NOT FAIR")
            else:
                if l[3]==l[5] and l[3]<l[4]:
                    print("FAIR")
                else:
                    print("NOT FAIR")
    else:
        b = (d[e[0]]<d[e[1]] and d[e[1]]<d[e[2]])
        if b:
            print("FAIR")
        else:
            print("NOT FAIR")
                
                