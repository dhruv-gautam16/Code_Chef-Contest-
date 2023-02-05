# cook your dish here
T = int(input())
while T:
    T -= 1
    N = int(input())
    S = input()
    l = [i for i in S]
    c1 = l.count("0")
    c2 = N - c1
    if c1 >= c2:
        print(c2)
    else:
        print(c1 + 1)