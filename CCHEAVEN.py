for _ in range(int(input())):
    n = int(input())
    s = input()
    g=b=flag=0
    for i in s:
        if int(i):
            g+=1
        else:
            b+=1
        if g>=b:
            flag=1
            break
    print("YES") if flag else print("NO")