# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    count = 0
    while len(arr)>1:
        if arr[0] == arr[-1]:
            del arr[0]
            del arr[-1]
        else:
            if arr[0]>arr[-1]:
                arr[0] = arr[0] - arr[-1]
                del arr[-1]
            else:
                arr[-1] = arr[-1] - arr[0]
                del arr[0]
            count = count + 1
        #print(arr)
    print(count)