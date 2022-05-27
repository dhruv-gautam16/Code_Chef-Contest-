for M in range(int(input())):
    a=int(input())
    l=list(map(int,input().split()))
    neg=0
    pos=0
    for i in l:
        if i%2==0:
            pos+=1
        else:
            neg+=1
    print(pos*neg)# cook your dish here
