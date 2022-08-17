# cook your code here
time = 60
fib = [0]*(time+1)
fib[0] = 0
fib[1] = 1
for i in range(2,time+1):
    fib[i] = fib[i-1]+fib[i-2]
    fib[i] %= 10
    
t = int(input())
for _ in range(t):
    n = int(input())
    most_pos = len(bin(n)[2:])
    pos = pow(2,most_pos-1,time)-1
    ans = fib[pos]
    print(ans)