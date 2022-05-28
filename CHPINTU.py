# cook your dish here
T=int(input())
for i in range(T):
    N,M=map(int,input().split())
    arrF=list(map(int,input().split()))
    arrP=list(map(int,input().split()))
    a={}
    m=10000000
    for i in range(N):
        a[arrF[i]]=a.get(arrF[i],0)+arrP[i] 
    for value in a.values():
        m=min(value,m)
    print(m)
    
    

    
    
