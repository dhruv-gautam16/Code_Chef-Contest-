# cook your dish here
T=int(input())
for i in range (T):
    X,Y=map(int,input().split())
    S=input()
    regular=S.count("1")
    l=[]
    c=0
    for j in range (len(S)):
        if S[j]=="1":
            c+=1
        else:
            c=0
        l.append(c)
    bonus=max(l)
    print((regular*X)+(bonus*Y))