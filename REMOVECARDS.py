# for t in range(int(input())):
#     N=int(input())
#     m=0
#     A=list(map(int,input().split()))
#     for i in range(N):
#         B=A.count(A[i])
#         if B>m:
#             m=B
#     print(N-m)
        
        
for t in range(int(input())):
    N=int(input())
    A=list(map(int,input().split()))
    D={}
    for i in A:
        if i not in D.keys():
            D[i]=0
        D[i]+=1
    B=max(D.values())
    print(N-B)