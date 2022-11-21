t = int(input())
while t > 0:
    n = int(input())
    r = 0
    ranswers = input()
    answers = input()
    i = 0
    penalty = False
    while i < n:
        if penalty:
            i += 1
            penalty = False
            continue
        elif 'N' == answers[i]:
            penalty = False
        elif answers[i] == ranswers[i] and (not penalty or i == n - 1):
            r += 1
        elif answers[i] != ranswers[i]:
            penalty = True
        i += 1
    print(r)
    t -= 1
