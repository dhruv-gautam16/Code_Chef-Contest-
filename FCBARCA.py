# cook your dish here
MOD = 1000000007
def main():
    t = int(input())
    for i in range(t):
        a,b = map(int,input().split())
        solve(a,b)

def solve(p,n):
    cache = [0]*(p+1)
    cache[0] = 0
    cache[1] = 0
    cache[2] = 1
    for i in range(3,p+1):
        cache[i] = ((n**(i-2)%MOD) - cache[i-1])%MOD
    print(n*cache[p]%MOD)

if __name__ == '__main__':
    main()