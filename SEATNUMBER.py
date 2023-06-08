t = int(input())
for i in range(t):
    n = int(input())
    if 1<=n<=10:
        print("lower double")
    elif 11<=n<=15:
        print("lower single")
    elif 16<=n<=25:
        print("upper double")
    else:
        print("upper single")