for _ in range(int(input())):
    arr = list(map(int,input().split(" ")))
    #seperating cost from array
    cost=arr[3]
    arr.pop()
    #sorting array and taking 2 highest values
    arr.sort()
    add=arr[1]+arr[2]
    
    #if the sum of 2 highest values can afford the subscription then certainly YES
    if add>=cost:
        print("YES")
    else:
        print("NO")