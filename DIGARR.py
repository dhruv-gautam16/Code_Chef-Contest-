def multiple5(digit,num):
    digit=int(digit)
    num=str(num)
    for i in range(digit):
        if(int(num[i])==0 or int(num[i])==5):
            print("YES")
            break
    else:
        print("NO")
        
    
t=int(input())
for j in range(t):
    digit=input()
    num=input()
    multiple5(digit,num)
