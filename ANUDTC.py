for tt in range(int(input())):
    N = int(input())
    if(360%N==0):
        x = "y"
    else:
        x = "n"
    if(N<=360):
        w = "y"
    else:
        w = "n"
    if((N*(N+1))/2) <=360:
        m = "y"
    else:
        m = "n"
    print(x,w,m,sep=" ")

         