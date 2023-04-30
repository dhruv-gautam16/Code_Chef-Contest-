for i in range(int(input())):
    n=int(input())
    #a=list(map(int,input().split()))
    m=2
    for i in range(n):
        for j in range(n):
            if m<=(n*n):
                print(m,end=" ")
            else:
                m=1
                print(m,end=" ")
            m+=2
        print()