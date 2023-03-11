from math import inf, lcm, gcd;
# ---------------------------------------- COLLECTIONS -----------------------------------------------#
from collections import defaultdict as maps #"""using this, we can give a default value of data type to dict"""
from collections import OrderedDict #"""this stores the order of insertion of values in dict"""
from collections import Counter as freq  #"""returns a dict containing count of values"""
from collections import ChainMap  #"""to have diff. dicts in one class (container)"""
#"""we have to use .new_child(new_dictToInsert) to insert a new dict into ChainMap"""
#---------------------------------------- COLLECTIONS ------------------------------------------------ #

def getlist():
    return list(map(int, input().split()))
    
def getinp():
    return map(int, input().split())
    
#----------------------------------------- MAIN CODE -------------------------------------------------#    
def main():
    for _ in range(int(input())):
        n, x = getinp()
        arr = getlist()
        odd = 0;
        for i in arr:
            if i & 1: odd += 1;
        even = n - odd;
        if x % 2 == 0 and even == n: print(-1);
        else:
            if even == 0: print(0)
            else:
                if x & 1:
                    if even & 1:
                        print(even//2 + 1)
                    else: print(even//2)
                else: 
                    print(even);
                
        
#----------------------------------------- MAIN CODE -------------------------------------------------#

if __name__ == "__main__":
    main()