# cook your dish here
t = int(input())

for i in range(t):
    n = int(input())
    a = 100 
    b = 100 
    for j in range(n):
        s = input()
        a = min(a, s.count('a'))
        b = min(b, s.count('b'))
    print(min(a, b))