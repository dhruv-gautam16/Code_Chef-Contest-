# cook your dish here
def prime(x):
    c=0
    for i in range(1,x+1):
        if x%i==0:
            c+=1
    if c==2:
        return("prime")
    else:
        return("not")
for _ in range(int(input())):
    A=list(map(int,input().split()))
    i=sum(A)+1
    f=0
    while(f==0):
        if prime(i)=="prime":
            f=-1
        i+=1
    print(abs(i-1-(sum(A))))