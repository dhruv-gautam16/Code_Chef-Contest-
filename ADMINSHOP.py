# cook your dish here
# cook your dish here
import math
 
T = int(input())
for i in range(T):
    n,x = map(int,input().split())
    A =  list(map(int,input().split()))
    min_element = min(A)
    print(max(math.ceil(x/min_element),n))