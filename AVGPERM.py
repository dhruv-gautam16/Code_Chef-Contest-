T = int(input())

for i in range(T):
    N = int(input())
    if(N==1):
        print("1")
    elif(N==2):
        print("2 1")
    elif(N==3):
        print("3 1 2")
    else:
        print(N,(N-2), end=" ", sep=" ")
        for i in range(1,N-3):
            print(i, end =" ")
        print((N-3),(N-1))