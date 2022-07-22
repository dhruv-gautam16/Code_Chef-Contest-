for _ in range(int(input())):
    x, y = map(int, input().split())
    
    if (x&1 and y&1) or x==1 or y==1:
        print(-1)
    else:
        if x&1:
            s1 = x//2*'a'+y//2*'b'+'a'+y//2*'b'+x//2*'a'
            s2 = y//2*'b'+x*'a'+y//2*'b'
        elif y&1:
            s1 = y//2*'b'+x//2*'a'+'b'+x//2*'a'+y//2*'b'
            s2 = x//2*'a'+y*'b'+x//2*'a'
        else:
            s1 = y//2*'b'+x*'a'+y//2*'b'
            s2 = x//2*'a'+y*'b'+x//2*'a'
            
        print(s1)
        print(s2)