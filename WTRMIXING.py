for testcases in range(int(input())):
    a,b,x,y=map(int,input().split())
    if(a>b):
        need=a-b 
        if(y>=need):print("YES")
        else: print("NO")
    elif b>a :
        need=b-a 
        if(x>=need): print("YES")
        else: print("NO")
    else : print("YES")