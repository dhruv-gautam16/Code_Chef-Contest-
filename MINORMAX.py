import bisect
import os, sys, math
from io import BytesIO, IOBase
from collections import defaultdict, deque

ip = lambda: input()
it = lambda: int(input())
ma = lambda: map(int, input().split())
li = lambda: list(map(int,input().split()))
MOD=10**9+7
MD=998244353
mod=100007
MIL=1000000
inf = float('inf')
ye = "YES"
ne = "NO"

def f(a, n, k):
    x = 0
    for i in range(n):
        x += a[i]//k
    print(x)

def main():
    for _ in range(it()):
        n = it()
        b = li()
        ans = ye
        if n == 1:
            print(ans)
            continue
        x, y = b[0], b[0]
        for i in range(1, n):
            if b[i] > x and b[i] < y:
                ans = ne
                break
            x = min(b[i], x)
            y = max(b[i], y)
        print(ans)
                

    # Fast IO Region
BUFSIZE = 8192
class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
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

def nc2(n):
    return (n*(n-1))//2

def ncr(n, r):
    if 2*r > n:
        return ncr(n, n - r)
    x = 1
    for i in range(r):
        x = x*(n - i)//(i + 1)
    return x

def segfunc(x,y):
  return x+y

class SegmentTree(object):
    def __init__(self, A, dot, unit):
        n = 1 << (len(A) - 1).bit_length()
        tree = [unit] * (2 * n)
        for i, v in enumerate(A):
            if v:
                tree[i + n] = 1
            #tree[i + n] = v
        for i in range(n - 1, 0, -1):
            tree[i] = dot(tree[i << 1], tree[i << 1 | 1])
        self._n = n
        self._tree = tree
        self._dot = dot
        self._unit = unit

    def __getitem__(self, i):
        return self._tree[i + self._n]

    def update(self, i, v):
        i += self._n
        self._tree[i] = v
        while i != 1:
            i >>= 1
            self._tree[i] = self._dot(self._tree[i << 1], self._tree[i << 1 | 1])

    def add(self, i, v):
        self.update(i, self[i] + v)

    def sum(self, l, r):
        l += self._n
        r += self._n
        l_val = r_val = self._unit
        while l < r:
            if l & 1:
                l_val = self._dot(l_val, self._tree[l])
                l += 1
            if r & 1:
                r -= 1
                r_val = self._dot(self._tree[r], r_val)
            l >>= 1
            r >>= 1
        return self._dot(l_val, r_val)


def merge(arr, left, mid, right):
    i = left
    j = mid
    k = 0
    invCount = 0
    temp = [0 for x in range(right - left + 1)]

    while (i < mid) and (j <= right):
        if arr[i] < arr[j]:
            temp[k] = arr[i]
            k += 1
            i += 1

        else:
            temp[k] = arr[j]
            invCount += mid - i
            k += 1
            j += 1

    while i < mid:
        temp[k] = arr[i]
        k += 1
        i += 1

    while j <= right:
        temp[k] = arr[j]
        k += 1
        j += 1

    k = 0
    for i in range(left, right + 1):
        arr[i] = temp[k]
        k += 1

    return invCount


def mergeSort(arr, left, right):
    invCount = 0

    if right > left:
        mid = (right + left) // 2

        invCount = mergeSort(arr, left, mid)
        invCount += mergeSort(arr, mid + 1, right)
        invCount += merge(arr, left, mid + 1, right)

    return invCount


def inversions(arr, n):
    return mergeSort(arr, 0, n - 1)


if __name__ == '__main__':
    main()