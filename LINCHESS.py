# cook your dish here
try:
    t=int(input())
    uni=list()
    def new(uni):
        l2=list()
        l3=list()
        l4=list()
        m,n=list(map(int,input().split(' ')))
        l1=list(map(int,input().split(' ')))[:m]
    #l2=list(filter(lambda x:(x*2<=n),l1))
        for i in range(len(l1)):
            if i+l1[i]+1<=n:
                l2.append(l1[i])
        for i in l2:
            if n%i==0:
                l3.append(i)
        if len(l3)==0:
            uni.append(-1)
        else:
            for i in l3:
                l4.append(i)
            uni.append(max(l4))
    for i in range(t):
        new(uni)
    for i in uni:
        print(i)
except:
    pass