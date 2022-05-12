# cook your dish here
for _ in range(int(input())):
    a = input()
    b = input()
    s = list(set(a))
    c=0
    for i in range(len(s)):
        c += min(a.count(s[i]),b.count(s[i]))
    print(c)
    
