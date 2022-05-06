# cook your dish here
t = int(input())
ans = []

for i in range(t):
    n = int(input())
    s = []
    for j in range(n):
        l=list(map(int,input().split()))
        s.append(l)
    c = s[0][0] + s[0][1]
    for k in range(1,len(s)):
        if c < s[k][0]:
            c += s[k][0] - c + s[k][1]
        elif c == s[k][0]:
            c += s[k][1]
        else:
            if (c - s[k][0]) % s[k][2] == 0:
                c += s[k][1]
            else:
                a = (c - s[k][0]) % s[k][2]
                c += (s[k][2] - a) + s[k][1]
    ans.append(c)
for z in ans:
    print(z)  