# cook your dish here
for i in range(int(input())):
    a,b = map(int, input().split())
    e = 2**b
    
    for i in range(1,a+1):
        e -= e/2
        
    print(int(e))