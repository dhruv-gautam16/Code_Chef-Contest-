for _ in range(int(input())):
    n = int(input())
    s = ''
    a = 'a'
    for i in range(n):
        if a=='z':
            a='a'
        s = s+a 
        a = chr(ord(a)+1)
    print(s)    