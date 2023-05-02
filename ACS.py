for _ in range(int(input())):
    n=int(input())
    r=n%100+n//100
    if r<=10:
        print(r)
    else:
        print("-1")