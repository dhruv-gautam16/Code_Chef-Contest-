# cook your dish here
# cook your dish here
#import 
"""def fact(x, s):
    
    d = [1]
    #print(s, x)
    for ii in range(2, x +1):
        d += [(d[-1]*ii)%(1000000007)]
    return d"""
d = [1]
#print(s, x)
for ii in range(2, 1000000 +1):
    d += [(d[-1]*ii)%(1000000007)]
for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    #s = set(a)
    #d = fact(max(s), s)
    
    ans = 0
    for xx in a:
        #print(xx, d)
        ans += d[xx-1]
    print(ans%(1000000007))