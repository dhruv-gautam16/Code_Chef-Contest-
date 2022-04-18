for _ in range(int(input())):
    l=list(map(int,input().split()))
    if ((l[0] == l[2]) and (l[1]==l[3])) :
        print(0)
    elif (((l[0]+l[1])%2 == 0 and (l[2]+l[3])%2 == 0)) or (((l[0]+l[1])%2 != 0 and (l[2]+l[3])%2 != 0)):
        print(2)
    else:
        print(1)