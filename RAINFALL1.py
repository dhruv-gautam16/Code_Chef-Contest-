for i in range(int(input())):
    x = int(input())
    if x < 3:
        print('Light')
    elif x < 7 and x >= 3:
        print('Moderate')
    else:
        print('Heavy')
