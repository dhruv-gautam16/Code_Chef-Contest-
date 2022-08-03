# cook your dish here
def solve(N,S):
    limit = 0
    for i in range(1,N+1):
        minn = (i*(i+1))//2+(N-i)
        maxx = (i*(i+1))//2+(N-i)*i
        
        if S>=minn and S<=maxx:
            limit = i
            
    ans = N-limit
    print(ans)
    
if __name__ == "__main__":
    t = int(input())
    for tc in range(t):
        N,S = map(int,input().split())
        solve(N,S)