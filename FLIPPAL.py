# cook your dish here
t=int(input())
i=0
while t>i:
    n=int(input())
    s=input()
    l=s.count("0")
    k=s.count("1")
    if n%2==0:
        if l%2==0 and k%2==0:
            print("yes")
        else:
            print("no")
    else:
        print("yes")
    i+=1