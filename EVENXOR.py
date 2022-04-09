a = []
for i in range(1,2004):
    if bin(i).count('1')%2==0:
        a.append(i)
for _ in range(int(input())):
    n = int(input())
    print(*a[:n])
