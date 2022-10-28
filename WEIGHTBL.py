# cook your dish here
T=int(input())
for i in range(T):
    w1,w2,x1,x2,M=map(int,input().split())
    a=w2-w1
    if(x1*M<=a and x2*M>=a):
        print("1")
    else:
        print("0")