# cook your dish here
m=list(map(int,input().split()))
l=[]
for i in m[1:]:
    if i%2==0:
        l.append((2**i-1)//3)
        l.append(2**i)
    else:
        l.append((2**i+1)//3)
        l.append(2**i)
for x in l:
    print(x,end=" ")