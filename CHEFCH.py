
def func(s):
    k = s[0]
    c = 0
    for i in range(1,len(s)):
        if (i%2 == 0 and s[i] != k):
            c += 1 
        elif (i%2 == 1 and s[i] == k):
            c += 1
    if c < len(s)-c:
        print(c)
    else:
        print(len(s)-c)
for _ in range(int(input())):
    s = input()
    func(s)

    
        
        
