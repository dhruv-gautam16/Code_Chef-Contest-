# cook your dish here
t = int(input())
for _ in range(t):
    s1 = input()
    s2 = input()
    
    n = len(s1)
    
    count = 0
    odd = None
    even = None
    
    for i in range(n):
        if i%2==0:
            if s1[i] != s2[i]:
                even = i
            else:
                if even != None:
                    count += 1
                even = None
                
        else:
            if s1[i] != s2[i]:
                odd = i
            else:
                if odd != None:
                    count += 1
                odd = None
                
    if odd != None:
        count += 1
    if even != None:
        count += 1
        
    print(count)