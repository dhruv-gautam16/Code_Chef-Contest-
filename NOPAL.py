# cook your dish here


if __name__ == "__main__":
    
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        curr = "a"
        res = ""
        for idx in range(n):
            res += curr 
            curr = chr(ord(curr) + 1)
            if curr == "d":
                curr = "a"
                
        print(res)