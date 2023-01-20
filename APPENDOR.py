# cook your dish here
T=int(input())
B=[]
A=[]
for i in range(T):
    B.append(input().split())
    A.append(input().split())

for i in range(len(A)):
    for j in range(len(A[i])):
        A[i][j]=int(A[i][j])

for i in range(len(B)):
    for j in range(len(B[i])):
        B[i][j]=int(B[i][j])

for i in range(T):
    a = A[i][0]
    for j in A[i]:
        a |= j
    a = bin(a)[2:]
    b = bin((B[i][1]))[2:]
    if len(a)>len(b) :
        for i in range(len(a)-len(b)):
            b="0"+b
    else :
        for i in range(len(b)-len(a)):
            a="0"+a
    c=""
    for i in range(len(a)):
        if b[i]=='0' and a[i]!='0':
            c=-1
            break
        else :
            if b[i]=='0' and a[i]=='0':
                c+="0"
            else :
                if b[i]=='1' and a[i]=='0':
                    c+="1"
                else :
                    c+="0"
    if c!=-1:
        print(int(("0b"+c),2))
    else :
        print(c)
            
    
    




    
    
    
