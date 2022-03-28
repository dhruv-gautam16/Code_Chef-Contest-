for _ in range(int(input())):
    d,x,y,z = map(int, input().split())
    normal_work = x*7
    first_hardwork = y*d + z*(7-d)
    print(max(normal_work, first_hardwork))