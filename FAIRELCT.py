for _ in range(int(input())):
    n,m=map(int,input().split())
    jhon=[int(i) for i in input().split()][:n]
    jack=[int(i) for i in input().split()][:m]
    ans=0
    flag=0
    while sum(jhon)<=sum(jack):
        min_ele=min(jhon)
        max_ele=max(jack)
        if min_ele<max_ele:
            i=jhon.index(min_ele)
            j=jack.index(max_ele)
            jhon[i]=max_ele
            jack[j]=min_ele
            ans=ans+1
        else:
            flag=1
            break
    if flag==0:
        print(ans)
    else:
        print(-1)