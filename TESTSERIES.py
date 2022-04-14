# cook your dish here
t = int(input())
for _ in range(t):
    a = list(map(int, input().split()))
    ci = a.count(1)
    ce = a.count(2)
    cd = a.count(0)
    if(ci>ce):
        print("INDIA")
    elif(ci<ce):
        print("ENGLAND")
    else:
        print("DRAW")