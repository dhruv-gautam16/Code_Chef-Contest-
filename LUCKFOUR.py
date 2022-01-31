t = int(input())
for i in range(t):
    fours = 0
    num = int(input())
    while(num):
        if(num%10 == 4):
            fours +=1
        num = int(num/10)
    print(fours)