# cook your dish here

for _ in range(int(input())):

    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    if(sum(a)==sum(b)):
        diff = 0
        for i in range(n):
            diff += abs(a[i]-b[i])
        print(diff//2)
    else:
        print(-1)