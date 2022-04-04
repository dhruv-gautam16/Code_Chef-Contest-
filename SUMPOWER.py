# cook your dish here

from sys import stdin, stdout
input = stdin.readline

if __name__ == "__main__":
    t = int(input().strip())
    
    for _ in range(t):
        n,k = list(map(int, input().strip().split()))
        s = input().strip()
        
        arr = list()
        psum = list()
        total = 0
        
        for i in range(n-1):
            if(s[i]==s[i+1]):
                arr.append(0)
            else:
                arr.append(1)
            
            total+=arr[i]
            psum.append(total)
            
            
        ans = psum[k-1]
        
        for i in range(k,n-1):
            ans+=(psum[i]-psum[i-k])
            
        print(ans)
                
            
                
        
        
        
        
