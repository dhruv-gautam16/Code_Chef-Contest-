# import math

# tc = int(input())
# for _ in range(tc):
#     A = list(map(int,input().split()))
#     n = A.pop(0)
#     hcf = math.gcd(*A)
#     for x in A:
#         ans = round(x/hcf)
#         print(ans,end=" ")
#     print()

def gcd (a,b):
    if (b == 0):
        return a
    else:
         return gcd (b, a % b)


tc = int(input())
for _ in range(tc):
    A = list(map(int,input().split()))
    n = A.pop(0)
    res = A[0]
    for c in A[1::]:
        res = gcd(res , c)
    
    for x in A:
        ans = round(x/res)
        print(ans,end=" ")
    print()
    