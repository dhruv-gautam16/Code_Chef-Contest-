
t=int(input())
for i in range(0,t):
    n,m=[int(x) for x in input().split()]
    onl=n/10
    k=n-onl
    if(m<k):
        print("DINING")
    elif(k<m):
        print("ONLINE")
    else:
        print("EITHER")