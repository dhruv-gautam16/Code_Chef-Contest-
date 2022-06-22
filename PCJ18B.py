# cook your dish here
T = int(input())
for i in range(T):
    N = int(input())
    print(sum([ (x)**2 for x in range(N, -2, -2) if x >= 1]))