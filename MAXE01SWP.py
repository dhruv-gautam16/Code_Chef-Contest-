
def inp():
    return int(input())
def st():
    return input().rstrip('\n')
def lis():
    return list(map(int,input().split()))
def ma():
    return map(int,input().split())

def solve(lent,binn):
    evens=binn[1::2]
    odds=binn[::2]
    odds0=odds.count('0')
    odds1=odds.count('1')
    evens0=evens.count('0')
    evens1=evens.count('1')
    val1=min(odds0,evens1)
    x=lent&1
    valid=max(0,lent//2 - val1 - 1+ x)
    val2=min(odds1,evens0)
    ans=val1+min(valid,val2)
    return ans
    

def main():
    for i in range(inp()):
        print(solve(inp(),st()))
if __name__=='__main__':
    main()