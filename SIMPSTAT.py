for _  in range(int(input())):
    n,k=map(int,input().split());
    l=list(map(int,input().split()));
    l.sort();
    sum1=c=0;
    if(k==0):
        print("%.6f"%(sum(l)/n));
    else:
        for i in range(n):
            if(i+1<=k or i>=n-k):
                c+=1;
                continue;
            sum1+=l[i];
        print("%.6f"%(sum1/(n-2*k)))
