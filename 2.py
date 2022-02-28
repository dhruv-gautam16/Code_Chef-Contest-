import sys
from collections import defaultdict
from math import gcd
from collections import deque

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)


if __name__ == "__main__":

    for t in range(int(input())):
        (a,b)=map(int,input().split())
        # d = list(map(int,input().split()))
