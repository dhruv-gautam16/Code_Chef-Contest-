# cook your dish here
for i in range(int(input())):
    n = int(input())
    s = input()
    a = []
    b = []
    
    for i in s:
        if i.isdigit():
            a.append(int(i))
        else:
            b.append(i)
    a.sort(reverse = True)
    b.sort()
    if len(b) == 1:
        for i in b:
            a.insert(-1,i)
    else:
        k = -(len(b))
        for i  in b:
            a.insert(k,i)
            k += 1
    result = ""
    
    for i in a:
        result += str(i)
    print(result)
        
            
            