# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    c = 0 
    for i in a:
        if i % 2 == 0:
            print("NO")
            c += 1
            break
    if c == 0:
        print("YES")