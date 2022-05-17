# cook your dish here
from itertools import product
for _ in range(int(input())):
    L,M =map(int,input().split())
    i = list(map(int,input().split()))
    #lst_2 = list(product(lst,repeat=2))
    i = list(set(i))
    i.sort(reverse = True)
    if len(i) == 1:
        print(2 * i[0])
    else:
        l = (i[0]-i[1])%M
        print(max(2*i[0],i[0]+i[1]+l,(i[0]+i[1])+M-l))
    #print(max(lst_3))
        