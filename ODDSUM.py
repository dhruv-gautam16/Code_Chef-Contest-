from sys import stdin
t = int(stdin.readline().strip())
while(t):
    n = int(stdin.readline().strip())
    if(n == 1 or n == 2):
        print(1)
    else:
        n -= 2
        print(1 + n * (n + 1))
    t -= 1