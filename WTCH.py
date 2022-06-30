# cook your dish here
t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    word = input()
    total = 0
    for i in range(n):
        if word[i] == '0':
            prev = (word[i-1] == '0') if (i != 0) else True
            next = (word[i+1] == '0') if (i != n-1) else True
            if prev and next: 
                total += 1
                word = word[:i] + '1' + word[i+1:]
            
    print(total)
