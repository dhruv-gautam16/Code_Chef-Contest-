try:
    n=int(input())
    for i in range(n):
        a = int(input())
        b = list(map(int,input().split()))
        print(sum(b)+max(b))
    
except:
    pass