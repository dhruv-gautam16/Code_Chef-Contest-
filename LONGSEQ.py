for tc in range(int(input())):
    n = input()
    x = n.count('1')
    y = n.count('0')
    if x == 1 or y == 1 :
        print("Yes")
    else :
        print("No")