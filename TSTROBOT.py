t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    s=input()
    a=[]
    a.append(x)
    for j in range(n):
        if s[j]=="R":
            x+=1
            a.append(x)
        else:
            x-=1
            a.append(x)
    a=list(dict.fromkeys(a))
    print(len(a))