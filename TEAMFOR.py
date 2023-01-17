# cook your dish here
# cook your dish here
# cook your dish here
for q in range(int(input())):
    n=int(input()) 
    a=input()
    b=input()
    sa=sb=0
    for i in a:
        if i=="1":
            sa+=1
    for j in b:
        if j=="1":
            sb+=1
    print(min(sa,sb,n//2))