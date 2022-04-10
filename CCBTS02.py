
for i in range(int(input())):
    flip=0
    input()
    L=input().split()
    for j in L:
        if j=='start' or j=='restart':
            flip=1
        elif j=='stop' and flip==1:
            flip=0
        elif j=='stop' and flip==0:
            print(404)
            break
    else:
        print(200)