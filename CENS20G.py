import sys
from collections import defaultdict
for _ in range(int(input())):
    s = sys.stdin.readline()
    x, y = map(int ,sys.stdin.readline().strip().split())
    q=int(sys.stdin.readline())
    dict = defaultdict(int)
    for i in s:
        dict[i] += 1
    for i in range(q):
        a,b=map(int ,sys.stdin.readline().strip().split())
        f=0
        c=0
        if a-x>=0:
            if dict["R"]>=(a-x):
                c+=a-x
            else:
                f=1
        else:
            if dict["L"]>=(x-a):
                c+=x-a
            else:
                f=1
        if b-y>=0:
            if dict["U"]>=(b-y):
                c+=b-y
            else:
                f=1
        else:
            if dict["D"]>=(y-b):
                c+=y-b
            else:
                f=1
        if f==0:
            sys.stdout.write("YES"+" "+str(c))
        else:
            sys.stdout.write("NO")
        sys.stdout.write("\n")