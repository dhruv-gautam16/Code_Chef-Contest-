r,b=input().split()
for j in range(int(r)):
    s=input()
    t=''
    for i in s:
        if i.isupper():
            t+=(b[ord(i.lower())-97]).upper()
        elif i.islower():
            t+=(b[ord(i)-97])
        elif i=='_':
            t+=' '
        else:
            t+=i
    print(t)