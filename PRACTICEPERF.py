
P = list(map(int,input().split()))
count = 0
for i in P:
    if i>=10:
        count = count + 1
print(count)
        