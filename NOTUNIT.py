T = int(input())
count = 0
while count<T:
    a, b = input().split(" ")
    i = int(a)
    j = int(b)
    if j-i<2:
        print("-1")
    else:
        if i%2 ==0:
            print(i,i+2)

        elif i%3 ==0:
            if j-i<=2:
                print("-1")
            else:
                print(i, i+3)
        else:
            if j-i<=2:
                print("-1")
            else:
                print(i+1, i+3)
        
    count = count + 1