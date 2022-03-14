for i in range(int(input())):
    a=int(input())
    b=a*2
    count=0
    for i in range(1,a+1):
        if i==i**2:
            count+=1
        else:
            continue
    print(count)
