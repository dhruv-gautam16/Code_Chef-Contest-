#!/usr/bin/env python
from cmath import inf
from itertools import permutations
from multiprocessing import heap
import os
import csv
import sys
from heapq import heapify, heappush, heappop
from collections import Counter
from io import BytesIO, IOBase
from bisect import bisect_right, bisect_left
from math import ceil
def gcd(a,b):
    a, b = max(a, b), min(a, b)
     
    # Everything divides 0
    if (b == 0):
         return a
    return gcd(b, a%b)

def lcm(a,b):
    a, b = max(a, b), min(a, b)
    return (a // gcd(a,b))* b
def modFact(n, p):
    if n >= p:
        return 0   
 
    result = 1
    for i in range(1, n + 1):
        result = (result * i) % p
 
    return result


def main():
    for i in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]
        count = 0
        for j in range(n):
            if arr[j] != arr[(j+1)%n]:
                count += 1
        one = arr.count(1)
        zero = n - one 
        minim = min(zero,one)
        if minim >= n//2:
            pot = n-n%2 
        else:
            pot = minim*2
        ans = pot - count
        if (ans//2)%2:
            print("Alice")
        else:
            print("Bob")
# region fastio

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._file = file
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion

if __name__ == "__main__":
    main()