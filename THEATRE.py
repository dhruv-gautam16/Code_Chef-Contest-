# cook your dish here
totals = []
for _ in range(int(input())):
    N = int(input())
    dp = [[0]*4 for i in range(4)]
    converter = {
        "A": 0,
        "B": 1,
        "C": 2,
        "D": 3,
        "12": 0,
        "3": 1,
        "6": 2,
        "9": 3
    }
    def smartsum(arr):
        z = sorted(arr, reverse=True)
        m = [25, 50, 75, 100]
        for i in range(len(z)):
            if z[i] == 0:
                z[i] = -100
            else:
                z[i] *= m.pop()
        return(sum(z))
    def helper(dp, list_ = [], sum_ = 0, depth = 0, vals = []):
        maxx = None
        if depth == 4:
            return vals
        for i in range(4):
            if i not in list_:
                new_sum = sum_ + dp[i][depth]
                x = helper(dp, list_ + [i], new_sum, depth + 1, vals + [dp[i][depth]])
                if maxx == None or smartsum(x) > smartsum(maxx):
                    maxx = x
        return maxx
    for i in range(N):
        A, B = list(input().split())
        dp[converter[A]][converter[B]] += 1
    z = helper(dp)
    z.sort(reverse = True)
    m = [25, 50, 75, 100]
    for i in range(len(z)):
        if z[i] == 0:
            z[i] = -100
        else:
            z[i] *= m.pop()
    totals.append(sum(z))
    print(sum(z))
print(sum(totals))