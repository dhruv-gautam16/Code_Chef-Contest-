T = int(input())
for j in range (T):
    N,B,M= map(int, input().split())
    integers = list (map(int, input().split()))
    count = 1 
    for i in range (M-1):
        if (integers[i+1] // B != integers[i] // B):
            count += 1
    print (count)
    