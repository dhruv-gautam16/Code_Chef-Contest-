for _ in range(int(input())):
    n,bob,ali = map(int,input().split())
    list_n = list(map(int,input().split()))
    b = 0
    a = 0
    for i in list_n:
        if i%bob == 0 and i%ali ==0:
            b += 1 
        elif i%bob == 0:
            b += 1 
        elif i%ali == 0:
            a += 1
    if b>a:
        print("BOB")
    else:
        print("ALICE")
        