for tc in range(int(input())):
    s = input()
    if len(s)== 1 or len(s)== 2 :
        print('YES')
    else:
        l = s[1:] +  s[0]
        r = s[-1:] + s[:-1]
        if l == r :
            print('YES')
        else :
            print('NO')