# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    count_odd = 0
    count_even = 0
    i = 0
    while i < n:
        if arr[i]%2 == 0:
            count_even = count_even + 1
        else:
            count_odd = count_odd + 1
        i = i + 1
    #print(count_even, count_odd)
    
    if count_odd%2==0 and count_odd>0:
        print('Yes')
    else:
        print('No')