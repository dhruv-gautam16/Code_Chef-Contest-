T=int(input())
for i in range(T):
    l,d,s,c = map(int,input().split())
    ans  = s 
    for a in range(2,d+1):
        ans = ans*(c+1)
        if ans>=l:
            break 
    if ans>=l:
        print("ALIVE AND KICKING")
    else:
        print("DEAD AND ROTTING")