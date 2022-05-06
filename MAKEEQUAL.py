# cook your dish here
T=int(input())
for i in range(T):
     N=int(input())
     A=list(map(int,input().split()))
     print(max(A)-min(A))