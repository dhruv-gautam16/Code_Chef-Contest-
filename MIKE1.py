# cook your dish here
n , m = map(int,input().split(" "))
arr = []
for i in range(n):
    arr.append([int(j) for j in input().split()])
l = int(input())
check = []
for i in range(l):
    a, b = map(int,input().split())
    check.append([a-1,b-1])

e1 , e2 = 0 , 0
for i in range(l):
    if e1 != -1:
        if check[i][0] < n and check[i][1] < m:
            e1 += arr[check[i][0]][check[i][1]]
        else:
            e1 = -1
    if e2 != -1:
        if check[i][0] < m and check[i][1] < n:
            e2 += arr[check[i][1]][check[i][0]]
        else:
            e2 = -1
print(max(e1,e2))# cook your dish here
