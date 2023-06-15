n=int(input())

for i in range(n):

    a,b=map(int,input().split())
    s=abs(a-b)
    if(s%3!=2):
        print("YES")
    else:
        print("NO")