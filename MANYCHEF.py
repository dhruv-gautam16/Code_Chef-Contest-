for _ in range(int(input())):
    s = input()
    n = len(s)
    
    def helper(i):
        return (i-3 >= 0 and (s[i]=='F' or s[i] == '?')
        and (s[i-1]=='E' or s[i-1] == '?')
        and (s[i-2]=='H' or s[i-2] == '?')
        and (s[i-3]=='C' or s[i-3] == '?'))
            
    
    
    res = ""
    i = n-1
    while i >= 0:
        
        if helper(i):
            res = "CHEF" + res
            i -= 4
            continue
        
        res = (s[i] if s[i] != '?' else 'A') + res
        i -= 1
        
    print(res)
            






# ? ? ? ? ? 
# c h e f

