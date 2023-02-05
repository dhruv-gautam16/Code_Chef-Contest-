# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    a = input()
    b = input()
    if a.count('1')==b.count('1'):
        print("YES")
    else:
        print("NO")