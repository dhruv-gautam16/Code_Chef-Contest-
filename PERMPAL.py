n=int(input())
for p in range(n):
    s=input()
    d={}
    for i in range(len(s)):
        lst=[]
        if s[i] in d:
            lst=d[s[i]]
            lst.append(i)
        else:
            lst=[i]
            d.update({s[i]:lst})
    ans=[0]*len(s)
    i=0
    j=len(s)-1
    count_o=0
    count_e=0
    for i in d.keys():
        if len(d[i])%2==0:
            count_e+=1
        else:
            count_o+=1
    #print(count_e,count_o)
    if count_o>1:
        print(-1)
    else:
        i=0
        j=len(s)-1
        for l in range(len(s)):
            lst=d[s[l]]
            if len(lst)%2==0:
                k=0
                while k<len(lst):
                    ans[i]=lst[k]+1
                    k+=1
                    ans[j]=lst[k]+1
                    k+=1
                    i+=1
                    j-=1
                lst=[]  
                d[s[l]]=lst
            else:
                k=1
                while k<len(lst):
                    ans[i]=lst[k-1]+1
                    k+=1
                    ans[j]=lst[k-1]+1
                    k+=1
                    i+=1
                    j-=1
                ans[len(s)//2]=lst[len(lst)-1]+1
                lst=[]
                d[s[l]]=lst
        print(*ans)