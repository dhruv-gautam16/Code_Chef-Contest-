import sys
from math import gcd, lcm, floor, ceil, factorial, comb, perm, sqrt, log
from collections import OrderedDict, namedtuple, Counter, deque
from statistics import mean, median, mode
from string import ascii_letters, ascii_lowercase, ascii_uppercase

mod = 1000000007
INF = float('inf')

def liststrip():
    return list(sys.stdin.readline().strip())
def intlistinp():
    return list(map(int, sys.stdin.readline().split()))
def strlistinp():
    return list(map(str, sys.stdin.readline().split()))
def inttupinp():
    return tuple(map(int, sys.stdin.readline().split()))
def strtupinp():
    return tuple(map(str, sys.stdin.readline().split()))
def intdeqinp():
    return deque(map(int, sys.stdin.readline().split()))
def strdeqinp():
    return deque(map(str, sys.stdin.readline().split()))
def intmapinp():
    return map(int, sys.stdin.readline().split())
def strmapinp():
    return map(str, sys.stdin.readline().split())
def inp():
    return sys.stdin.readline()
def intinp():
    return int(sys.stdin.readline())
def bininp():
    return int(sys.stdin.readline(), 2)
def println(n):
    return sys.stdout.write(str(n)+"\n")
def printsl(n):
    return sys.stdout.write(str(n)+" ")
    
# Use List for indexing else use deque

def solve(n, s):
    s1 = list(s[0::2])
    s2 = list(s[1::2])
    s1.sort()
    s2.sort()

    if s1 == s2:
        println('YES')
    else:
        println('NO')


for _ in range(intinp()):
    n = intinp()
    s = input()

    solve(n, s)