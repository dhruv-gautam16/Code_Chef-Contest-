for i in range(int(input())):
    p = int(input())
    step = 0
    for i in range(11, -1, -1):
        res = 2 ** i
        while(p >= res):
            p -= res
            step += 1
    print(step)