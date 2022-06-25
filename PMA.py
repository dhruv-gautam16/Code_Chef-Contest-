# cook your dish here
for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    
    A = list(map(abs, A))
    even = A[::2]
    odd = A[1::2]
    s1, s2 = sum(even), sum(odd)
    t1, t2 = max(odd), min(even)
    if t1 > t2:
        s1 += - t2 + t1
        s2 += - t1 + t2
    print(s1 - s2)