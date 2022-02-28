n = int(input())
for _ in range(n):
    s = input()
    s = s + s[0]
    red = 0
    green = 0
    for i in range(len(s)-1):
        if(s[i] == s[i+1]):
            if(s[i] == 'R'):
                red+=1
            else:
                green+=1
    if((red == 1 and green == 1) or (red == 0 and green ==0)):
        print("yes")
    else:
        print("no")