t = int(input())

for i in range(t):
    p,q = map(int, input().split())
    a = p+q
    if a % 4 == 1 or a % 4 ==0:
        print('Alice')
    else:
        print('Bob')
        