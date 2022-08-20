# cook your dish here
t = int(input())

for i in range(t):
    b = int(input())
    a = b
    c = b | (1 << 28)
    d = b | (1 << 29)
    print(a, c, d)