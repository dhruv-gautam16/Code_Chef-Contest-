import math

# cook your dish here
for _ in range(int(input())):
    N, K = [ int(x) for x in input().split() ]
    S = input().strip()
    
    a = S.count("1")
    b = len(S) - a
    
    t = abs(a - b)
    
    print(math.ceil(t / K))