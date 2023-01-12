# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    B = list(map(int,input().split()))
    
    Bdict = {}
    for i in B:
        if i in Bdict:
            Bdict[i] += 1
        else:
            Bdict[i] = 1
    
    #print(Bdict)
    
    flag = 0
    for i in Bdict:
        if (Bdict[i]%i)!=0:
            flag = 1
    
    if flag==1:
        print(-1)
    else:
        dictcount = {}
        dictassign = {}
        A = []
        j = 1
        for i in B:
            if i in dictcount:
                A.append(dictassign[i])
                dictcount[i] += 1
                if dictcount[i]==i:
                    del dictcount[i]
            else:
                dictcount[i] = 1
                dictassign[i] = j
                A.append(j)
                if dictcount[i]==i:
                    del dictcount[i]
                j = j + 1
        print(*A)
            
            