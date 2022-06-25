for _ in range(int(input())):
    D, d, P, Q=map(int,input().split())
    totalMoney=0
    i=0
    ind=0
    rem=D%d
    mul=D//d
    p=mul*P
    # temp=
    totalMoney=d*(p+Q*((mul-1)*(mul))//2)
    # while(i!=D-rem):
        
    #     totalMoney+=d*(P+ind*Q)
    #     ind+=1
    #     # print(totalMoney)
    #     i+=d 
    totalMoney+=rem*(P+(mul)*Q)
    print(totalMoney)