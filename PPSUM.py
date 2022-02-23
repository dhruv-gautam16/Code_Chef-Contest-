t = int(input())
for _ in range(t):
    D,N = list(map(int,input().split()))
    cr = N
    for i in range(D):
        cr = (cr*(cr+1))//2
    print(cr)