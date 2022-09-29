tc = int(input())
for k in range(tc):
    n, t = input().split()
    n, t = int(n), float(t)
    arr = []
    for j in range(n):
        arr.append(float(input()))
    l = 0.0
    r = 10.0 ** 12
    mn = r
    while (True):
        mid = l + (r - l) / 2
        if ( (r - l) <= 0.0001):
            mn = mid 
            break
        right = None
        flag = True
        for i in range(n -1 , -1 , -1):
            if (i == n - 1):
                right = arr[n - 1] + mid - t
            else:
                if (arr[i] <= right):
                    pos = min(arr[i] + mid, right)
                    right = pos - t
                else:
                    pos = max(arr[i] - mid, right)
                    if (pos > right or pos < 0):
                        flag = False
                        break
                    right = pos - t
        if (flag == True):
            r = mid 
        else:
            l = mid
    num = str(round(mn, 4)).split(".")
    while (len(num[1]) < 4):
        num[1] += "0"
    print(".".join(num))