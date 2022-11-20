for _ in range(int(input())):
    A,B = map(int,input().split())
    if B<=A:
        print(B)
    else:
        print(B%(A+1))