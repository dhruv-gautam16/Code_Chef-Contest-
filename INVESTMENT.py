# cook your dish here
T = int(input())
for tc in range(T):
    # x=Interest, y=Inflation
    (x, y) = map(int, input().split(' '))
	
    if x/y >= 2:
        print('YES')
    else:
        print('NO')
	