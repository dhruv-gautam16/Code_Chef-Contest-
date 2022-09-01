n, m = list(map(int, input().split()))
a = input().split()
b = input().split()
for i in range(len(a)):
    a[i] = int(a[i])
for i in range(len(b)):
    b[i] = int(b[i])
smol = a[0]
for i in range(len(a)):
    if smol > a[i]:
        smol = a[i]
cnt = 0
for i in range(len(b)):
    if b[i] < smol:
        cnt += 1
print(cnt * n)