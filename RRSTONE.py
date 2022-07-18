# cook your dish here

n,k = map(int,input().split())
a = list(map(int,input().split()))
if k == 0:
    k = 0
elif k%2 == 1:
    k = 1
else:
    k = 2
for i in range(k):
    max1 = max(a)
    for i in range(len(a)):
        a[i] = max1 - a[i]
for i in range(len(a)):
    print(a[i],end = " ")