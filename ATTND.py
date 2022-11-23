# cook your dish here
T = int(input())
for _ in range(T):
    N = int(input())
    f_list = []
    l_list = []
    for i in range(N):
        f, l = map(str, input().split())
        f_list.append(f)
        l_list.append(l)
    for i in range(N):
        if f_list.count(f_list[i]) > 1:
            print(f_list[i], l_list[i])
        else:
            print(f_list[i])