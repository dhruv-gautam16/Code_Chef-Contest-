# cook your dish here
def solve():
    n,p=map(int,input().split())
    s=str()
    s+='a'
    s+='b'*(p-2)
    s+='a'
    print(s*(n//p) if p>2 else 'impossible')
for _ in range(int(input())):
    solve()