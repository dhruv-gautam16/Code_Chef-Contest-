for _ in range (int(input())):
    n,k=map(int,input().split())
    lt=list(map(int,input().split()))
    st=""
    for i in lt:
        if i%k==0:
            st+="1"
        else:
            st+="0"
    print(st)