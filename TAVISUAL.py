for _ in range(int(input())):
        #t=int(input())
        a,b,t=map(int,input().split())
        c=b
        for i in range(t):
            l,m=map(int,input().split())
            if c<=m and c>=l:
                c=l-c+m
            #print(c)
        print(c)
# cook your dish here
