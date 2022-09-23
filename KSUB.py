# cook your dish here
import math

def isKGoodArray(nums, k):
    
    arrayGcd = 0
    for num in nums:
        arrayGcd = math.gcd(arrayGcd, num)
    
    subarrayGcd = 0
    numSubarrays = 0
    for i in range(len(nums)):
        subarrayGcd = math.gcd(nums[i], subarrayGcd)
        if subarrayGcd == arrayGcd:
            subarrayGcd = 0
            numSubarrays += 1
    
    return numSubarrays >= k
    
numTestCases = int(input())
for i in range(numTestCases):
    n, k = [int(i) for i in input().split(" ")]
    nums = [int(i) for i in input().split(" ")]
    result = "YES" if isKGoodArray(nums, k) else "NO"
    print(result)
        
    
    

