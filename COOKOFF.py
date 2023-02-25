for _ in range(int(input())):
    n = int(input())
    d = {'cakewalk': 0, 'simple': 0, 'easy': 0, 'easy-medium': 0, 'medium': 0, 'medium-hard': 0, 'hard': 0}
    for i in range(n):
        d[input()] += 1
    if d['cakewalk'] > 0 and d['simple'] > 0 and d['easy'] > 0 and (d['easy-medium'] > 0 or d['medium'] > 0) and (d['medium-hard'] > 0 or d['hard'] > 0):
        print('Yes')
    else:
        print('No')