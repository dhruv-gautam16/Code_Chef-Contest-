# cook your dish here
def solve():
    #code here
    n,x = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    total = sum(arr)
    
    maxi, sum_ = 0, 0
    for i in range(n):
        sum_+=arr[i]
        maxi = max(sum_,maxi)
        if sum_ <= 0:
            sum_ = 0
    return total-maxi+(maxi/x)
    #sum1+sum_max+sum2-sum_max+sum_max//x
print(solve())
    
    