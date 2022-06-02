
for _ in range(int(input())):
    x = input()
    y = input()
    ans=''
    for i in range(len(x)):
        if x[i]==y[i]=='W' or x[i]=='W' or y[i]=='W':
            ans+='B'
        else:
            ans+='W'
    print(ans)