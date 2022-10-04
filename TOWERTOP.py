# cook your dish here
from math import ceil

def moves_to_build(h):
    moves = 1
    while h>1:
        h = ceil(h/2)
        moves += 1
    return moves
    
T = int(input())

for i in range(T):
    h, moves = map(int,input().split())
    print(max(0, 1+ moves - moves_to_build(h)))