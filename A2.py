# cook your dish here
tn = int(input())
for _ in range(tn):
    k = int(input())
    arr = list(map(int,input().split()))
    
    if k == 1:
        if arr[0] == 1:
            print("Yes")
        else:
            print("No")
    
    else:
        sli = arr[-1]//2
        for i in range(k-2,0,-1):
            sli = ((sli+arr[i])//2)
        if sli == 1:
            print("Yes")
        else:
            print("No")