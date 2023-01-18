# cook your dish here
# cook your dish here
from collections import defaultdict
v="aeiou"
for _ in range(int(input())):
    n=int(input())
    s=str(input())
    p=str(input())
    d=defaultdict(lambda:0)
    dd=defaultdict(lambda:0)
    ans=0
    # f=0
    m1=0
    m2=0
    c1=0
    c2=0
    for i,j in zip(s,p):
        if i==j:
            if i=="?":f=1
            continue
        if i!="?" and j!="?":
            x=(int(i in v) + int(j in v))
            if x==1:ans+=1
            else:ans+=2
            # print(i,j,ans)
            continue
        elif i=="?":
            if j not in v:
                c2+=1
                dd[j]+=1
                m2=max(m2,dd[j])
            else:
                c1+=1
                d[j]+=1
                m1=max(m1,d[j])
            
        elif j=="?":
            if i not in v:
                c2+=1
                dd[i]+=1
                m2=max(m2,dd[i])
            else:
                c1+=1
                d[i]+=1
                m1=max(m1,d[i])
    # print(m1,m2,c1,c2,ans)
    ans+=min(2*(c1-m1)+c2,2*(c2-m2)+c1)
    print(ans)