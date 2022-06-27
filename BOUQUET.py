# cook your dish here
for i in range(int(input())):
    MG,MY,MR=map(int,input().split(" "))
    OG,OY,OR=map(int,input().split(" "))
    PG,PY,PR=map(int,input().split(" "))
    
    color=max(MR+OR+PR,max(MG+OG+PG,MY+OY+PY))
    tree=max(PG+PY+PR,max(MG+MY+MR,OG+OY+OR))
    
    ans=max(color,tree)
    
    if ans==0:
        pass
    elif ans%2==0:
        ans=ans-1
    print(ans)