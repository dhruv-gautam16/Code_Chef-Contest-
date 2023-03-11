for _ in range(int(input())):
    input()
    s = input()
    i = s.find('0')
    if i == -1:
        print(len(s))
        continue
    t = s[i : ]
    print(max(len(u) for u in t.split('0')) + i)
