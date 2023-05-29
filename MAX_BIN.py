mapInput = lambda: map(int, input().split())
listInput = lambda: list(mapInput())
ceil = lambda x, y: -(-x//y)
binary = lambda x: bin(x)[2:]

for _ in range(int(input())):
    n, k = mapInput()
    s = input()
    if(s[0] == '1'):
        for i in range(k):
            s = s + '0'
    else:
        for i in range(k-1):
            s = s + '0'
        s = '1' + s[1:]
    print(s)