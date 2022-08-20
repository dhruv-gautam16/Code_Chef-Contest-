for _ in range(int(input())):
    k=int(input())
    mat=[[0 for i in range(k)] for j in range(k)]
    mat[k//2]=[i for i in range(1,k+1)]
   # print(mat)
    z=[i for i in range(1,k+1)]
    j=1
    for i in range(k//2+1,k,1):
        mat[i]=z[j:]+z[:j]
        j+=1 
   # print(mat)
    j=k-1 
    for i in range(k//2-1,-1,-1):
        mat[i]=z[j:]+z[:j]
        j-=1 
    for i in range(k):
        print(*(mat[i]))