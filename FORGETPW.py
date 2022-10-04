T = int(input())
for _ in range(T):
    N = int(input())
    data = dict() 
    for __ in  range(N):
        ci, pi = input().split() 
        data[ci] = pi
    S = list(input())
    for i in range(len(S)):
        if S[i] in data.keys():
            S[i] = data[S[i]] 
    S = "".join(S)
    if '.' in S:
        S = S.strip('0').rstrip('.')
    else:
        S = S.lstrip('0')
    print(S or '0')