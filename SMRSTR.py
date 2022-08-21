
# cook your dish here
T=int(input())
for i in range(T):
    N,Q=list(map(int,input().split()))
    D=list(map(int,input().split()))
    Qseries=list(map(int,input().split()))
    temp=1
    for num in D:
        temp*=num
    ans=''
    for Qsub in Qseries:
        if(len(ans)==0):
            ans=str(Qsub//temp)
        else:
            ans+=' '+str(Qsub//temp)
    print(ans)