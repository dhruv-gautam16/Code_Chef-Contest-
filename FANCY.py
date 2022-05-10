n=int(input())
for i in range(n):
    s=input().split()
    f=list(s)
    if 'not' in f:
        print('Real Fancy')
    else:
        print("regularly fancy")