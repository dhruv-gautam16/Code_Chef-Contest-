
base = int(1e9) + 7
ways = [0, 1, 2]
for i in range(3, int(1e6)):
    ways.append((ways[-1] + ways[-2]) % base)
    
for _ in range(int(input())):
    steps, guess = map(int, input().split())
    M = ways[steps]
    M %= int(1e9) + 7
    set_bits = bin(M).count("1")
    if set_bits == guess:
        print("CORRECT")
    else:
        print("INCORRECT")
