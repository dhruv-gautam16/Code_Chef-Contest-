# cook your dish here
# cook your dish here
def lcs(s, r):
    n, m = len(s), len(r)
    prev, curr = [0]*(m+1), [0]*(m+1)
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s[i-1]==r[j-1]:
                curr[j] = 1+prev[j-1]
            else:
                if curr[j-1]>prev[j]:
                    curr[j] = curr[j-1]
                else:
                    curr[j] = prev[j]
        curr, prev = prev, curr
    return prev[m]

t=int(input())
for i in range(t):
    n = int(input())
    s = input()
    r = s[::-1]
    print(lcs(s,r)//2)