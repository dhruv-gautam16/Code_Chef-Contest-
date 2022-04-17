t = int(input())

for _ in range(t):
    n = int(input())
    
    store = {l:0 for l in 'codehf'}

    for _ in range(n):
        for char in input():
            if char in store:
                store[char] += 1
                
    
    store['c'] //=  2
    store['e'] //= 2
    
    print(min(store.values()))# cook your dish here