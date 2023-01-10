t = int(input())
for _ in range(t):
    S = str(input())
    zeroone = S.count('01')
    onezero = S.count('10')
    if zeroone == onezero:
        print(len(S)-2)
    else:
        print(2)