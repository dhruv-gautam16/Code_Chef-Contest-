# cook your dish here
n = int(input())
for i in range(n):
    x = input()
    mark = 1
    
    if x.count('P') == 1:
        if x.count('C') == 1:
            if x.count('M') == 1:
                print("YES")
            else:
                mark = 0
        else:
            mark = 0
    else:
        mark = 0
        
    if mark==0:
        print("NO")