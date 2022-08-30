# cook your dish here
N = int(input())
ll = [int(x) for x in input().split()]
q =int(input())
sum1= sum(ll)
for _ in range(q):
    sum1 = 2*sum1
    print(sum1%(10**9+7))

