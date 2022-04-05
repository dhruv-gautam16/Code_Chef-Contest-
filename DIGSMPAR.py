def check(n):
    st=str(n)
    s=0
    for i in st:
        s+=int(i)
    return s%2

for i in range(int(input())):
    n = int(input())
    if check(n)==check(n+1):
        print(n+2)
    else:
        print(n+1)