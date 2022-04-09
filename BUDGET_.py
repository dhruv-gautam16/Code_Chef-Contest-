t= int(input())
for i in range(0,t):
    salary,rupee = map(int,input().split(" "))
    exp = rupee*30
    if exp<salary:
        print("YES")
    elif exp>salary:
        print("NO")
    else :
        print("YES")

    

