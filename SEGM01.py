t=int(input())
for i in range (0,t):
    s=input()
    s.split()
    l=[]
    c=0
    for j in range (0,len(s)):
        if(s[j]=="1"):
            l.append(j)
            c=c+1
    if(len(l)==0):
        print("NO")
    else:
        p=len(l)-1
        k=(l[p]-l[0])+1
        if(k==c):
            print("YES")
        else:
            print("NO")