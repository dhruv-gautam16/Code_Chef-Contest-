T = int(input())
inputs = [input().split() for y in range(T)]

total = 0
for a,b in inputs:
    print(eval(a) % eval(b))