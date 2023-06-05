 
for i in range(int(input())):
    a=int(input())
    m=0
    for i in range(1,a+1):
        if (a%i)==0:
            m=m+1
     
    if m==2:
        print("yes")
    else:
        print("no")
