# cook your dish here
for _ in range(int(input())):
    s = input()
    n = len(s)
    if n < 10:
        print('NO')
    else:
        l = [False]*4
        flag = False
        if 'a' <= s[0] <= 'z' or 'a' <= s[-1] <= 'z':
            l[0] = True
        for i in range(1,n-1):
            if s[i].isnumeric():
                l[1] = True
            elif 'A' <= s[i] <= 'Z':
                l[2] = True
            elif 'a' <= s[i] <= 'z':
                l[0] = True
            else:
                l[3] = True
            if l == [True]*4:
                flag = True
                break
        if flag:
            print('YES')
        else:
            print("NO")