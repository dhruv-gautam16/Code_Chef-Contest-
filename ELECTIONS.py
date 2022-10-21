# cook your dish here
t= int(input())
for i in range(t):
    a,b,c=map(int,input().split(" "))
    maxm=max(a,b,c)
    
    if maxm>50:
        if maxm == a:
            print("A")
        elif maxm == b:
            print("B")
        elif maxm == c:
            print("C")
    else:
        print("NOTA")
        