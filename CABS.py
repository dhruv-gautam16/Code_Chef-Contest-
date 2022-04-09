T=int(input())
for i in range(T):
    x,y=map(int , input().split())
    if x<y:
        print("FIRST")
    elif x==y:
        print("ANY")
    else:
        print("SECOND")
