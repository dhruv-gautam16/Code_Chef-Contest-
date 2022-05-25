# cook your dish here
for i in range(int(input())):
    n,a,b=map(int,input().split())
    if n<3:
        print(0)
        continue
    elif min(a,b)>1 and max(a,b)<n and abs(a-b)==1:
        print(2)
    elif abs(a-b)==2:
        print(1)
    elif abs(a-b)==1  and (min(a,b)==1 or max(a,b)==n):
        print(1)
    else:
        print(0)
    