# cook your dish here
# cook your dish here
t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    pr_even = [0]*n
    curr_even = 0
    for i,j in enumerate(arr):
        if j & 1:
            pr_even[i] = curr_even
        else:
            curr_even += 1
            pr_even[i] = curr_even
    
    q = int(input())
    for i in range(q):
        l,r = list(map(int,input().split()))
        ev = pr_even[r-1]-pr_even[l-1]
        if arr[l-1] % 2 == 0:
            ev += 1
        if ev > 0:
            print("EVEN")
        else:
            print("ODD")
        
        