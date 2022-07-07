
for t in range(int(input())):
    n=int(input())
    for i in range(n):
        x,y=map(int,input().split())
    chord=n
    while n>5:
        n=n//2
        chord+=n
    print(chord)