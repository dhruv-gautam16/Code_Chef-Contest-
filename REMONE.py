from heapq import heapify, heappush, heappop



T = int(input())
for i in range(T):
    n = int(input())
    A1=list(map(int,input().split(" ")))
    A = [i * (-1) for i in A1]
    B1=list(map(int,input().split(" ")))
    B = [i * (-1) for i in B1]
    heapify(A)
    heapify(B)
    if n==2:
        base = 0-heappop(B)
        can1 = base+heappop(A)
        can2 = base+heappop(A)
        if can1>0  and can1 < can2:
            print(can1)
        else:
            print(can2)
    else:
        a1 = 0-heappop(A)
        a2 = 0-heappop(A)
        a3 = 0-heappop(A)
        b1 = 0-heappop(B)
        b2 = 0-heappop(B)
        if b1-a1<=0:
            print(b1-a2)
        elif b1-a1 == b2-a2 or b1-a1 == b2-a3:
            print(b1-a1)
        else:
            print(b1-a2)