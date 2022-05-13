# cook your dish here
def subseq(a,b):
    n1,n2 = len(a),len(b)
    i = 0
    j = 0
    while i < n1 and j < n2:
        if a[i] == b[j]:
            i += 1
            j += 1
        else:
            j += 1
    if i >= n1:
        return True
    else:
        return False
T = int(input())
for _ in range(T):
    a,b = map(str,input().split())
    if subseq(a,b) or subseq(b,a):
        print("YES")
    else:
        print("NO")