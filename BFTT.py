# cook your dish here
for j in range(int(input())):
    n=int(input())
    while True:
        m=n+1 
        m=str(m)
        a=list(m)
        if a.count('3')>=3:
            print(m)
            break
        else:
            n+=1