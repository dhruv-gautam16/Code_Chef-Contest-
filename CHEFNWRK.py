    # cook your dish here
for _ in range(int(input())): 
    n,k = map(int,input().split()) 
    list_a = list(map(int,input().split())) 
    sum = 0 
    result = 1 
    for char in list_a: 
        if char > k: 
            result = -1 
            break 
        elif char <= k: 
            sum += char 
            if sum <= k: 
                continue 
            elif sum > k: 
                result += 1 
                sum = char 
    print(result)