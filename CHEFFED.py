n = int(input())
count = 0
k = max(n//3,n-90)
for i in range(k,n):
    a = i 
    b = sum([int(j) for j in str(a)])
    c = sum([int(k) for k in str(b)])
    if a + b + c == n:
        count += 1 
print(count)