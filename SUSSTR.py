# cook your dish here
for i in range(int(input())) :
    n = int(input())
    a = input()
    s = []
    k = 0
    
    for i in range((n+1)//2) :
        if a[i] == "1" :
            s.append("1")
        else :
            s.insert(0, "0")
            
        if n%2 == 1 and i == (n + 1)//2 - 1 :
            break
        
        if a[n - i - 1] == "1" :
            s.insert(0, "1")    
        else :
            s.append("0")
    c = ""      
    for i in s :
        c += i
    print(c)            