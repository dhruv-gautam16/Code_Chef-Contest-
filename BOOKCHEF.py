n,m = map(int,input().split())
a = list(map(int,input().split(" ")))
special = []
normal = []
for _ in range(m):
    f,p,s=input().split()
    f = int(f); p = int(p)
    if f in a:
        special.append((p, f, s))
    else: 
        normal.append((p, f, s))
special.sort(reverse = True)
normal.sort(reverse = True)
for i in special:
        print(i[2])
for i in normal:
        print(i[2])
