t=int(input())
sum=0
for i in range(t):
    (a,b,c)=map(int,input().split(' '))
    arr=[]
    arr.append(a)
    arr.append(b)
    arr.append(c)
    arr.sort()
    print(arr[1])
    
        
