# cook your dish here
lim = 2500*2500//4+1
acc = [0 for _ in range(lim+10)]
def precompute():
    global acc, lim
    cnt = [0 for _ in range(lim+10)]
    for i in range(1, lim+1):
        for j in range(i, lim+1, i):cnt[j] += 1
    for i in range(1, lim+1):acc[i] = acc[i-1]+cnt[i]
def solve(N):
    global acc, lim
    ret = 0
    for i in range(1, N):ret += acc[i*(N-i)-1]
    return ret
precompute()
for _ in range(int(input())):
    print (solve(int(input())))