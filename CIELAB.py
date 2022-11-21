for i in range(int(input())):
    a=int(input())
    arr=list(map(int,input().split()))
    if 1 in arr:
        print("CHEF")
    else:
        if sum(arr)%2==0:
            print("CHEFINA")
        else:
            print("CHEF")