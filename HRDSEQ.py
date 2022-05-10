# cook your dish here
for _ in range(int(input())):
    n = int(input())
    li = [0,0]
    x = 0
    for i in range(2,n):
        if li.count(li[i-1]) >= 2:
            k = li[:i-1]
            k.reverse()
            p = li[i-1]
            ind = len(li) - k.index(p) - 1
            li.append(i-ind)
            
        else:
            li.append(0)
    c=0
    for i in range(n):
        if li[i] == li[n-1]:
            c += 1 
    print(c)


        
