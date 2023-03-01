for _ in range(int(input())):
    x=int(input())
    s=""
    for i in range(x):
        if i%2==0:
            s+="1 "
        else:
            s+="0 "
    print(s[:-1])