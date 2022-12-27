# cook your dish here
for i in range(int(input())):
    a = input()
    b = input()
    s = 0 
    t = 0 
    for j in range(len(a)):
        if a[j] == "0":
            s+= 1 
        else:t+= 1 
    #print(s,t)
        if b[j]=="0":
            s+= 1 
        else: t+=1 
    u = min(s,t)
    #print(u)
    st = ""
    for k in range(0,u):
        st += "1"
    for l in range(u,len(a)):
        st += "0" 
    print(st)    