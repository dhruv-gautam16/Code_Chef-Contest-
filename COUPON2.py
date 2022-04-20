for _ in range(int(input())):
    d, c=map(int, input().split())
    a=list(map(int, input().split()))
    b=list(map(int, input().split()))
    t=sum(a)+sum(b)+2*d 
    tp=0
    if sum(a)>=150 and sum(b)>=150:
        tp=sum(a)+sum(b)+c 
    elif sum(a)<150 and sum(b)<150:
        tp=sum(a)+sum(b)+2*d 
    else:
        tp=sum(a)+sum(b)+c+d 
    if tp<t:
        print("YES")
    else:
        print("NO")