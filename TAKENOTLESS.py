# cook your dish here
def fun(a):
    c={}
    b=set(a)
    if len(b)==1:
        if len(a)%2==0:
            return("Zenyk")
        else:
            return("Marichka")
    else:
        if len(b)==len(a):
            return("Marichka")
        else:
            for i in a:
                if c.get(i) is None:
                    c[i] = 1
                else:
                    c[i]+=1
            for i in c.values():
                if i % 2 == 1:
                    return("Marichka")
            return("Zenyk")
    
for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    print(fun(a))