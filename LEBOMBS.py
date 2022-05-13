for item in range(int(input())):
    kp=int(input())
    pen=input()
    yan=[1]*kp
    for l in range(kp):
        if pen[l]=="1":
            yan[l]=0
            if l!=0:
                yan[l-1]=0
            if l!=(kp-1):
                yan[l+1]=0
    print(yan.count(1)) 