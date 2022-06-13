# cook your dish here
t = int(input())
for _ in range(t):
   u,v = map(int,input().split())
   sm = u+v 
   ans = (sm*(sm+1))//2+u+1 
   print(ans)