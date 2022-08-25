testCases = int(input())
for i in range(testCases, 0, -1):
    num, k = map(int, input().split())
    
    digits = [int(a) for a in str(num)]
    for i in range(k):
        if (min(digits) == 9):
            break
        else:
            digits[digits.index(min(digits))] = min(digits) + 1
    prod = 1
    
    for i in digits:
        prod *= i
        
    print(prod)