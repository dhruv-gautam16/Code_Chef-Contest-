# cook your dish here
for i in range(int(input())):
    N,K,M=map(int,input().split())
    if(N%(K*M)==0):
        print(N//(K*M))
    else:
        N=N//(K*M)
        print(N+1)