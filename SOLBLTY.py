for _ in range(int(input())):
    x,a,b = map(int,input().split())
    ans1 = (a+(100-x)*b)*10
    print(ans1)