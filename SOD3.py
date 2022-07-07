# cook your dish here
for _ in range(int(input())):

    L,R = map(int,input().split())

    S,E = 0,0

    # for S

    if L % 3 == 0:

        S = L

    elif L % 3 == 1:

        S = L + 2

    elif L % 3 == 2:

        S = L + 1

    # for E

    if R % 3 == 0:

        E = R

    elif R % 3 == 1:

        E = R - 1

    elif R % 3 == 2:

        E = R - 2

    if S == E:

        print(1)

    elif S > E:

        print(0)

    else:

        print(((E-S)//3) + 1)