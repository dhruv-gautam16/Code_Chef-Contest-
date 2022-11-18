# cook your dish here
p=int(input())
for i in range(p):
    m=input()
    n=[]
    for i in m:
        if i.isdigit():
            n.append(int(i))
    print(sum(n))