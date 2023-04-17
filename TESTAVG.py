
hlo=int(input())
for love in range(hlo):
    l=list(map(int,input().split()))
    if (l[0]+l[1])/2>=35 and (l[2]+l[1])/2>=35 and (l[0]+l[2])/2>=35 :
        print("pass")
    else:
        print("fail")