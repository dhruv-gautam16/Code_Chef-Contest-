# cook your dish here
import numpy as np

T=int(input())

for case in range(T):
    N=int(input())
    M=np.zeros((N,N))

    for i in range(N):
        l=str(input())
        for j in range(N):
            if l[j]=='#':
                M[i,j]=1 
    #ligne south-north
    M1=np.copy(M)
    for i in range(N-2,-1,-1):
        M1[i,:]=M1[i+1,:]+M1[i,:]
    #ligne east-west
    M2=np.copy(M)
    for j in range(N-2,-1,-1):
        M2[:,j]=M2[:,j+1]+M2[:,j]
    print(N*N-np.count_nonzero(M1+M2))

    