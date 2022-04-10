for t in range(int(input())):
    N, K = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    problems_solved = 0
    too_slow = False
    is_bot = True
    for i in range(N):
        problems_solved += int(A[i] != -1)
        if (A[i] > K):
            too_slow = True
        if (A[i] > 1):
            is_bot = False
    is_bot = is_bot and (problems_solved == N)
    if (problems_solved < N/2):
        print('Rejected')
    elif (too_slow):
        print('Too Slow')
    elif (is_bot):
        print('Bot')
    else:
        print('Accepted')
