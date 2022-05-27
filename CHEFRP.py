for i in range(int(input())):
        n = int(input())
        a = list(map(int, input().split(" ")))
        total = 0
        a.sort()
        if 1 in a:
                print(-1)
        elif n == 1 and a[0]>1:
                print(2)
        else:
                for x in range(n-1,0,-1):
                      total+= a[x]
                total+=2
                print(total)
                