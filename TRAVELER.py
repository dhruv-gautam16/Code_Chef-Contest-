# cook your dish here
import math

N=int(input())
city=[x for x in input().split()]
M=int(input())
route = {}
for m in range(M):
    r = [x for x in input().split()]
    route[(r[0],r[1])]=int(r[2])

T=int(input())

for t in range(T):
   cur_route = [x for x in input().split()]
   K=int(cur_route[0])
   cur_route=cur_route[1:]
   if not all([x in city for x in cur_route]):
       print("ERROR")
       continue
   if len(set(cur_route)) != len(cur_route):
       print("ERROR")
       continue

   ans = 0

   for i in range(K-1):
       if (cur_route[i],cur_route[i+1]) in route:
           ans+=route[(cur_route[i],cur_route[i+1])]
       else:
           print("ERROR")
           break
   else:
       print(ans)