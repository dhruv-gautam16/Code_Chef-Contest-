# cook your dish here
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    s=str(input())
    lo,hi=0,n-1
    cnt=0
    if n==1:
        print("YES")
    else:
        while lo<=hi:
            if s[lo]!=s[hi]:
                cnt+=1
            lo+=1
            hi-=1
        if cnt>k:
            print("NO")
        elif cnt==k:
            print("YES")
        else:
            x=k-cnt
            if n%2!=0:
                print("YES")
            else:
                if x%2==0:
                    print("YES")
                else:
                    print("NO")