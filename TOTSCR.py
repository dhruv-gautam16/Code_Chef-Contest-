# cook your dish here
t=int(input())
while(t>0):
    N,K=[int(x) for x in input().split()]
    points=[int(x) for x in input().split()]
    while(N>0):
        count=0
        score=input()
        for i in range(len(score)):
            if score[i]=="1":
                count+=points[i]
        print(count)
        N-=1
    t-=1
