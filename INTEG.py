# cook your dish here
n = int(input())
l = map(int, input().split())
x = int(input())
l = [i for i in l if i < 0]
l.sort()
print(-sum(l) if -sum(l) <= x else -sum(l[:x]))