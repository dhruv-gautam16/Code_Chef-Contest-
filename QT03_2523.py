for _ in range(int(input())):
    n=int(input())
    s=input()
    s1=set(s)
    if len(s1)==len(s):
        print(-1)
    else:
        print(len(s)-2)
        
    
        
