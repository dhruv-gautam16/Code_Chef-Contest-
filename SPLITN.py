for i in range(int(input())):
    n=int(input())
    c=0
    while(n>1):
        if(n%2==1):
            c+=1 
        n=n//2
    print(c)