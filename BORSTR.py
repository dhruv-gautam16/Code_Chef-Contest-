# cook your dish here
t=int(input())
for j in range(t):
    n=int(input())
    s=input()
    Max=0
    d={}
    for i in range(n):
        if s[i] not in d:
            d[s[i]]=[1,1]
            k=1
        else:
            if prev==s[i]:
                k+=1
                if k>d[prev][0]:
                    d[prev][0]=k 
                    d[prev][1]=1 
                elif k==d[prev][0]:
                    d[prev][1]+=1
            else:
                if d[s[i]][0]==1:
                    d[s[i]][1]+=1
                k=1
        prev=s[i]
    Max=[]
    for i in d:
        if d[i]>Max:
            Max=d[i]
    if Max[1]==1:
        print(Max[0]-1)
    else:
        print(Max[0])