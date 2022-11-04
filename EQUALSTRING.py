for _ in range(int(input())):
    n=int(input())
    a=input()
    b=input()
    al=[]
    count=0
    for i in range(n):
        if a[i]!=b[i]:
           al.append(b[i])
    al=set(al)
    print(len(al))