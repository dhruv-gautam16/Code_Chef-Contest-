a,b=map(int,input().split())
lh=[]
lv=[]
bye=0
l=[]
for i in range(a):
    t=list(map(int,input().split()))
    lh.append(t)
for i in range(b):
    for m in range(a):
        l.append(lh[m][i])
    lv.append(l)
    l=[]
#print(lv)
for i in range(a):
    for j in range(b):
        if lh[i][j]==min(lh[i])and lh[i][j]==max(lv[j]):
            t=1
            print(lh[i][j])
            break
    if t==1:
        break
else:
    print('GUESS')
 # cook your dish here
