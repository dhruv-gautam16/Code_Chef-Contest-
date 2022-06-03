# cook your dish here
t = int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    xor=0
    for i in l:
        xor^=i
    print(2*xor)