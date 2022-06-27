# cook your dish here
case=int(input())
for _ in range(case):
    N=int(input())
    string=input()
    Left=0
    right=0
    canhelp=False
    for letter in string:
        if letter=='L':
            Left+=1
            right=0
        elif letter=='R':
            right+=1
            Left=0
        if right==2 or Left==2:
            canhelp=True
            break
    if canhelp==True:
        print("YES")
    else:
        print("NO")
        print