# cook your dish here
for _ in range(int(input())):
    n = int(input())
    s = input()
    ans = n
    for i in range(1, n):
        if s[i] == '0':
            ans = i
            break
        
    
    print(ans)