# cook your dish here
for _ in range(int(input())):
    x,y=map(int,input().split())
    n=list(map(int,input().split()))
    s=[]
    n.sort()
    j=0
    while y<=x:
        s.append(n[y-1]-n[j])
        j+=1
        y+=1
    print(min(s)) 
