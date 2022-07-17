# cook your dish here
for _ in range(int(input())):
    c=int(input())
    b=bin(c)[2:]
    o=[]
    for i in range(len(b)):
        if i==0:
            o.append('1')
        else:
            if b[i]=='1':
                o.append('0')
            else:
                o.append('1')
    n1=int("".join(o),2)
    n2=c^n1
    print(n1*n2)