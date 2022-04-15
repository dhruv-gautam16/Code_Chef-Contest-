# cook your dish here
for i in range(int(input())):
    l=[0,0,0,0,0,0,0,0,0,0]
    x=0
    for i in range(int(input())):
        s=input()
        for i in range(len(s)):
            if s[i]=='1':
                l[i]+=1
    for j in l:
        if j%2==1:
            x+=1
    print(x)