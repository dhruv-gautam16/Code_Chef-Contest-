# cook your dish here
def isSubsetSum(arr, n, target):
    if target == 0:
        return True
        
    if n == 0:
        return False
        
    if arr[n-1] > target:
        return isSubsetSum(arr, n-1, target)
        
    return isSubsetSum(arr, n-1, target) or isSubsetSum(arr, n-1, target-arr[n-1])
        
    
    
for _ in range(int(input())):
    n, m = map(int, input().split())
    notes = []
    for _ in range(n):
        notes.append(int(input()))
        
    if isSubsetSum(notes, n, m):
        print('Yes')
    else:
        print('No')
        
    