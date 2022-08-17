# cook your dish here
# cook your dish here
x=int(input())
for _ in range(x):
    n=input()
    lol=[]
    for i in n:
        if i!="=":
            lol.append(i)
    n="".join(lol)        
    l=0
    if len(n)>0:
        l+=1
        c=1
        for i in range(1,len(n)):
            if n[i]==n[i-1]:
                c+=1
            else:
                #print(c,l,i)
                l=max(l,c)
                c=1
        l=max(l,c)    
    print(l+1)