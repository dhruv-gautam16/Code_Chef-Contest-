# cook your dish here
t= int(input())
for i in range (t):
    n,x = map(int, input().split())
    ans='NO'
    if x%2 ==1:
        ans ="YES"
    else:
        if n%2==0:
            ans = "YES"
    print(ans)    