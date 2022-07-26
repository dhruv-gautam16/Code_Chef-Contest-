t=int(input())

while(t>0):
    s=int(input())
    q=list(map(int,input().split()))
    time=0
    for i in range(s):
        e=list(map(int,input().split()))
        for j in range(e[0]):
            if(j==0):
                time+=e[1]
            else:
                time+=(e[j+1]-q[i])
    print(time)
    t-=1