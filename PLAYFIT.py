t=int(input())
for q in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    ma=l[0]
    c=0
    for i in range(1,n):
        v=l[i]-ma
        if(l[i]<ma):
            ma=l[i]
        if(v>c):
            c=v
        
    if(c>0):
        print(c)
    else:
        print("UNFIT")

# for i in range(int(input())):
#     n=int(input())
#     l=list(map(int,input().split()))
#     minn=l[0]
#     count=0
#     for i in range(1,n):
#         val=l[i]-minn
#         if(l[i]<minn):
#             minn=l[i]
#         if(val>count):
#             count=val
#     if(count>0):
#         print(count)
#     else:
#         print("UNFIT")

            