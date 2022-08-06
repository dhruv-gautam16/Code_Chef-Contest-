# cook your dish here
# cook your dish here
import bisect

for _ in range(int(input())):
    n=int(input())
    nli=list(map(int,input().split()))
    nli.sort()
    q=int(input())
    for i in range(q):
        x,y=map(int,input().split())
        sm=x+y
        m=bisect.bisect(nli,sm)
        if m>0:
            if nli[m-1]==sm:
                print(-1)
            else:
                print(m)
        else:
            print(0)