# cook your dish here
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def sol(arr, n):
    ans = 0
    pref_gcd, suff_gcd = [0]*n, [0]*n

    for i in range(n):
        if i == 0:
            pref_gcd[i] = arr[i]
        else:
            pref_gcd[i] = gcd(pref_gcd[i-1], arr[i])

    for i in range(n-1, -1, -1):
        if i == n-1:
            suff_gcd[i] = arr[i]
        else:
            suff_gcd[i] = gcd(suff_gcd[i+1], arr[i])
    # suff_gcd = suff_gcd[::-1]

    for i in range(n):
        curr_gcd = 0
        if i == 0:
            curr_gcd = suff_gcd[i+1]
        elif i == n-1:
            curr_gcd = pref_gcd[i-1]
        else:
            curr_gcd = gcd(pref_gcd[i-1], suff_gcd[i+1])
        if curr_gcd != 1:
            ans += 1
    return ans
    # cook your dish here
    
t = int(input())
while t:
    n = int(input())
    arr_s = input().split()
    arr = []
    for i in arr_s:
        arr.append(int(i))
    print(sol(arr, n))
    t -= 1
    