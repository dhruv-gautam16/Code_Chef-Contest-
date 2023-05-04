# cook your dish here
for _ in range(int(input())):
    n = int(input())
    if n > 4:
        f = n//5
        print(n-f)
    else:
        print(n)