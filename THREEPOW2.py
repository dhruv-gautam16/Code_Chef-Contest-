# cook your dish here
for _ in range(int(input())):
    n=int(input())
    s=input()
    if s=="1" or s=="10":
        print("NO")
    else:
        num=0
        for i in s:
            if i=="1":
                num+=1
        if num<=3:
            print("YES")
        else:
            print("NO")
    
