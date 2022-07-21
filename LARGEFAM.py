n=int(input())
for j in range(n):
    num=int(input())
    l=list(map(int,input().split()))
    c=0
    true=0
    l.sort()
    for i in l:
       c=c+i
       if(c<=(num-1)):
          true+=1
    print(true)  
        