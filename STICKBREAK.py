# cook your dish here
for i in range(int(input())):
    l,k=map(int,input().split())
    if(l%k==0):
        print(0)
    else:
        print(1)