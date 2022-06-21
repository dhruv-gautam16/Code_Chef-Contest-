t = int(input())
for _ in range(t):
    n = int(input())
    if n%26 != 0 or n == 0:
        p = n//26
    elif n%26 == 0:
        p = int(n/26 - 1)
    k = 2**p 
    d = n - (p*26)
    if d <=2:
        print('{} 0 0'.format(k))
    elif 2 < d <= 10:
        print('0 {} 0'.format(k))
    elif 10 < d <= 26:
        print('0 0 {}'.format(k))