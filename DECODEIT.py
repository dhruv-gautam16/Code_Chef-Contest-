def get_char(code):
    
    first = ["a", "b", "c", "d", "e", "f", "g", "h"]
    last = ["i", "j", "k", "l", "m", "n", "o", "p"]
    
    if code[0] == "0":
        result = first
    else:
        result = last
    if code[1] == "0":
        result = result[:4]
    else:
        result = result[4:]
    if code[2] == "0":
        result = result[:2]
    else:
        result = result[2:]
    if code[3] == "0":
        result = result[0]
    else:
        result = result[1]
    return result
for _ in range(int(input())):
    l = int(input())
    code = input()
    letters = []
    code = list([i for i in code])
    t = 0
    u = 4
    for i in range(l//4):
        t = code[t:u]
        letters.append(t)
        t = u
        u += 4
    final_ans = []
    for i in letters:
        final_ans.append(get_char(i))
    print("".join(final_ans))
