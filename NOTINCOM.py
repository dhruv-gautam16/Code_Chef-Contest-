# cook your dish here
t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    a = set(a)
    b = set(b)
    c = a&b 
    print(len(c))