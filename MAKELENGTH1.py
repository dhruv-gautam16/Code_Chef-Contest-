# cook your dish here
for i in range(int(input())):
    n = int(input())
    s = input()
    flag = False
    if n == 1:
        print('YES')
    else:
        count = 0
        for i in s:
            if i == '1':
                count+=1 
            else:
                if count%2 == 1:
                    flag = True
                    print('NO')
                    break
                count = 0
        if flag != True:
            if count %2 == 0:
                print("YES")
            else:
                print("NO")
            