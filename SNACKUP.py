# cook your dish here
from collections import deque


for _ in range(int(input())):
    n=int(input())
    q=deque()
    for i in range(n):
        q.append((i+1,(i+1)%n +1))
    print(n)
    for _ in range(n):
        print(n)
        for i, (x,y) in enumerate(q,start=1):
            print(i,x,y)
        q.append(q.popleft())