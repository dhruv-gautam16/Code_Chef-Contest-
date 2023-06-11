for i in range(int(input())):
    a, b = map(int, input().split(" "))
    if a == b:
        print("Yes")
    else:
        # check if the number can be achieved or not 
        mini = min(a,b)
        maxi = max(a,b)
        
        while(mini<maxi):
            mini *= 2
            
        if mini == maxi:
            print("Yes")
        else:
            print("No")