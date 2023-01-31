# cook your dish here
debug = False
def debug_msg(*args, **kwargs):
    if debug:
        print(*args, **kwargs)

T = int(input())
for temp in range(T):
    N, D = map(int, input().split())

    new_N = N
    current_digit = 1
    
    debug_msg(f"N={N}, D={D}")
    while new_N >= current_digit:
        debug_msg(f"current_digit={current_digit}")
        digit = (new_N // current_digit) % 10

        if digit==D:
            if current_digit == 1:
                new_N += 1
                current_digit *= 10
            else:
                new_N = ((new_N // current_digit) + 1) * current_digit
                current_digit = 1
        else:
            current_digit *= 10
                
        debug_msg(f"new_N={new_N}")
    print(new_N-N)