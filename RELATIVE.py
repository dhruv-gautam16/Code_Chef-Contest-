# cook your dish here
n=int(input())
for i in range(n):
    g,c=map(int,input().split())
    print(int((c**2)/(2*g)))