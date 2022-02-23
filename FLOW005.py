try:
    for _ in range(int(input())):
        n=int(input())
        count=0
        while n:
            if n>=100:
                count+=1
                n-=100
            elif n>=50:
                count+=1
                n-=50
            elif n>=10:
                count+=1
                n-=10
            elif n>=5:
                count+=1
                n-=5
            elif n>=2:
                count+=1
                n-=2
            elif n>=1:
                count+=1
                n-=1
        else:
            print(count)
            
except:
    pass