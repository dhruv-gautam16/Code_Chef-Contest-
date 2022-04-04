for _ in range(int(input())):
    s = input()
    t = input()
    x = []
    xd = {}
    for i in range(len(t)):
        if t[i].isupper(): 
            x += [1]
            xd[t[i].lower()] = xd.setdefault(t[i].lower(), 0) + 1
        elif t[i].isalpha(): 
            x +=[0]
            xd[t[i]] = xd.setdefault(t[i], 0) + 1
        else:
            x += [-1]
    xd = sorted(xd.items(), key = lambda x: (x[1], x[0]))
    ans = {}
    for i in range(len(xd)):
        ans[xd[i][0]] = s[26-len(xd)+ i]
    for i in range(len(t)):
        if t[i].isalpha():
            if x[i] == 0:
                print(ans[t[i]], end = "")
            else:
                print(ans[t[i].lower()].upper(), end = "")
        else:
            print(t[i], end = "")
    print()