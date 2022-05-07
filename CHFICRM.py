for i in range(int(input())):
    n = int(input())
    m = list(map(int,input().split()))
    box5 = []
    box10 = []
    box15 = []
    op = "YES"
    for i in m:
        re = i-5
        if re==10:
            if len(box10)>0:
                box10 = box10[1:]
                box15.append(1)
            elif len(box5)>1:
                box5 = box5[2:]
                box15.append(1)
            else:
                op = "NO"
                break
        elif re == 5:
            if len(box5)>0:
                box5 = box5[1:]
                box10.append(1)
            else:
                op = "NO"
                break
        else:
            box5.append(1)
    print(op)