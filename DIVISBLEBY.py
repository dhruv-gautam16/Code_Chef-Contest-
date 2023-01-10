# cook your dish here
# cook your dish here
import math
# def gcd(a,b):
#     while(b):
#         a,b=b,a%b
#     return a
t=int(input())
for x in range(t):
    n=int(input())
    a=[int(c) for c in input().split()]
    final_gcd=a[0]
    for i in a:
        final_gcd=math.gcd(final_gcd,i)
    for i in a:
        print(i//final_gcd,end=" ")
    print()