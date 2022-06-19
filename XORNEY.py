# cook your dish here
for _ in range(int(input())):
    l,r=map(int,input().split())
    count=0
    if l%2==0 and r%2==0:
        count=(r-l)//2
    else:
        count=(r-l)//2+1
    if count%2==0:
        print("Even")
    else:
        print("Odd")