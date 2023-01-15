# cook your dish here
# cook your dish here

# cook your dish here


def divisors(a):
    ans=[]
    for i in range(1,int(a**0.5) + 1):
        if a%i==0:
            ans+=[[i,a//i]]
    return ans
for _ in range(int(input())):
    [x,y]=[int(i) for i in input().split()]
    d=divisors(y)
    low=x//2
    high=low
    if x&1:
        high+=1
    flag=0
    for i in d:
        if high < i[0] or low > i[1]:
            print(low,high)
            print(*i)
            flag=1
            break
    if flag==0:
        print(-1)