dt={};lt=[]
for _ in range (sum(list(map(int,input().split())))):
    ip=int(input())
    if ip in dt.keys():
        dt[ip]+=1
    else:
        dt[ip]=1
for i,j in dt.items():
    if j>1:
        lt.append(i)
print(len(lt))
lt.sort()
for i in lt:
    print(i)