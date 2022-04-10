for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    count1,count2=0,0
    for i in a:
        if(i%2==0):count1+=1 
        else:count2+=1 
    print(n-count2) if count2>count1 else print(n-count1)    