# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    print(max([-(-sum(a[:i+1])//(i+1)) for i, e in enumerate(a)]))