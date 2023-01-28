# cook your dish here


T = int(input())

for i in range(T):
    s = input()
    t = input()
    u1 = set(s) - set(t)
    u2 = set(t) - set(s)
    for j in (u1):
        if s.count(j) > 1:
            x = 1
            break
        else:
            x = 0
    if not u1:
        print("B")
    elif u1 and not u2:
        print("A")
    elif x == 1:
        print("A")
    else:
        print("B")