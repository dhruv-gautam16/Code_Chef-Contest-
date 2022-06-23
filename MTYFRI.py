# cook your dish here
for _ in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    m=[l[i] for i in range(0,n,2)]
    t=[l[i] for i in range(1,n,2)]
    sm=sum(m)
    st=sum(t)
    j=sm-st
    if st>sm:
        print("YES")
        continue
    elif k==0:
        print("NO")
        continue
    else:
        while k>0 and st<=sm:
            sm1=max(m)
            st1=min(t)
            sm=sm-sm1+st1
            st=st-st1+sm1
            if sm-st>=j:
                print("NO")
                break
            j=sm-st
            k-=1
        else:
            if k==0 and st<=sm:
                print("NO")
            else:
                print("YES")