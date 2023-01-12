# cook your dish here
# cook your dish here
# cook your dish here
for i in range(int(input())) :
    n =int(input())
    s = input()
    s1 = input()
    a,b = set(s),set(s1)
    l = []
    for i in a :
        if i in b :
            l.append(min(s.count(i),s1.count(i)))
    if l!=[] :
        
        print(max(l))        
    else :
        print(0)