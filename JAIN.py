# cook your dish here
import itertools
power_set = ["".join(map(str, k)) for k in map(list, itertools.product([0, 1], repeat=5))]

def get_bitmask(S):
    indexes = {"a": 0, "e": 1, "i": 2, "o": 3, "u": 4}
    bitmask = [0]*5
    for ch in S:
        bitmask[indexes[ch]] = 1
    return 

def get_mask(S):
    indexes = {"a": 0, "e": 1, "i": 2, "o": 3, "u": 4}
    mask = 0
    for ch in S:
        mask += 2 ** indexes[ch]
    return mask
    
def find_union(x, y):
    res = ""
    for p,q in zip(x, y):
        res += str(int(p) or int(q))
    return res
    
    
for i in range(int(input())):
    N = int(input())
    di_set = []
    dp = [0]*(32)
    for _ in range(N):
        mask = get_mask(set(input()))
        dp[mask] += 1 
        
    likes_dishes = 0
    for i in range(32):
       for j in range(i+1,32):
          if i | j == 31:
             likes_dishes+= dp[i]*dp[j]
       
    likes_dishes+=dp[31]*(dp[31]-1)//2
    print(likes_dishes)

