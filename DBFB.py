# cook your dish here
# cook your dish here
mod=1000000007
def multiply(mat1,mat2):
    mat3=[[0,0],[0,0]]
    mat3[0][0]=(mat1[0][0]*mat2[0][0]+mat1[0][1]*mat2[1][0])
    mat3[0][1]=(mat1[0][0]*mat2[0][1]+mat1[0][1]*mat2[1][1])
    mat3[1][0]=(mat1[1][0]*mat2[0][0]+mat1[1][1]*mat2[1][0])
    mat3[1][1]=(mat1[1][0]*mat2[0][1]+mat1[1][1]*mat2[1][1])
    return mat3
def power(mat,n):
    if(n==0):
        a=[[1,0],[0,1]]
        return a
    if(n==1):
        return mat
    y=power(mat,(int)(n//2))
    if(n&1):
        return multiply(mat,multiply(y,y))
    else:
        return multiply(y,y)
t=int(input())
for i in range(t):
    m,n=map(int,input().split())
    l1=list([(int)(x) for x in input().split()])
    l2=list([(int)(x) for x in input().split()])
    d1=dict()
    d2=dict()
    f1=0
    f2=0
    for j in range(0,m):
        f1+=l1[j]
        f2+=l2[j]
    f1=(m*f1)%mod
    f2=(m*f2)%mod
    ans=0
    mat=[[1,1],[1,0]]
    if(n==1):
        print(f1%mod)
    elif(n==2):
        print(f2%mod)
    elif(n>2):
        mat=power(mat,n-2)
        ans=mat[0][0]*f2+mat[0][1]*f1
        print(ans%mod)
    
