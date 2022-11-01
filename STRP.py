# cook your dish here
for _ in range(int(input())):
    n = int(input())
    s = input()
    c = 0
    i = 0
    while(i < len(s)):
        c = c + 1
        if(i != n-1 and s[i] == s[i + 1]):
            i = i + 2
        else:
            i = i + 1
    print(c)