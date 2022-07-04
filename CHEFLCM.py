# cook your dish here
def inparr():
    tmparr = [int(i) for i in input().split()]
    return tmparr
for _ in range(int(input())):
    N = int(input())
    if N==1:
        print(1)
    elif N==2:
        print(3)
    else:
        lim = int(N**0.5)+1
        summ =1+N
        for i in range(2,lim):
            if N%i==0:
                tmp2 = N//i
                if i!=tmp2:
                    summ+=i+tmp2
                else:
                    summ+=i
        print(summ)