# cook your dish here
t = int(input())
for _ in range(t):
    x, y, z = map(int, input().split(" ", 3))
    k = max(x, y, z)
    if k == x:
        print("Setter")
    if k == y:
        print("Tester")
    if k == z:
        print("Editorialist")
