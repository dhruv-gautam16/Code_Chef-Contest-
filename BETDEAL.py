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
        a,b = getinp()
        # after disc
        a = 100 - int(100 * (a/100));
        b = 200 - int(200 * (b/100));
        if a < b: print("First") 
        elif b < a: print("Second")
        else: print('Both')
        
#----------------------------------------- MAIN CODE -------------------------------------------------#

if __name__ == "__main__":
    main()