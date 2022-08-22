# cook your dish here
import collections as clts
import math
import heapq

def gcd(x,y):
    if y == 0:
        return x
    else: return gcd(y,x%y)
def lcm(x,y): return int(x/gcd(x,y)*y)

for _ in range(int(input())):
    graph = {
        'R': ['R','B'],
        'B': ['Y','B'],
        'Y': ['P','B'],
        'P': ['G','B'],
        'G': ['R','B']
    }
    
    S = input()
    curr = 'R'
    for edge in S:
        curr = graph[curr][int(edge)]
    if curr != 'G':
        print("NO")
    else: print("YES")
    
    
    