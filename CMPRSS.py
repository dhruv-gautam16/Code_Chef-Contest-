for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    s=''
    i=0
    while(i<n):
        if i!=0:
            s+=','
        j=i
        cnt=1
        while j<n-1 and a[j]+1==a[j+1]:
            cnt+=1
            j+=1
        if cnt>=3:
            s+=str(a[i])+'...'+str(a[j])
            i=j+1
        else:
            s+=str(a[i])
            i+=1
    print(s)