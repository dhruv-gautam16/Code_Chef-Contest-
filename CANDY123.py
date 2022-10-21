# cook your dish here
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    l=bo=0
    for i in range(1,(a+b)+1):
        if(i%2!=0):
            l+=i
        else:
            bo+=i
        if(l>a):
            print('Bob')
            break
        elif(bo>b):
            print('Limak')
            break