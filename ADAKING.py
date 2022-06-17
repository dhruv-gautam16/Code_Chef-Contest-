# cook your dish here
for _ in range(int(input())):
    d = int(input())
    for p in range(8):
        for q in range(8):
            if p == 0 and q == 0:
                print('O',end = '')
                d -= 1
            elif d == 0:
                print('X',end = '')
            else:
                print('.',end = '')
                d -= 1
        print()
