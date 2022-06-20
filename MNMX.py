# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(i) for i in input().split()]
    arr.sort()
    print(arr[0]*(n-1))