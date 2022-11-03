# cook your dish here
for _ in range(int(input())):
    N = int(input())
    mx = 0
    for __ in range(N):
        new = int(input())
        if new > mx : mx = new
    print(mx)