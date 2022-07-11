import math
tcase = int(input().rstrip())# cook your dish here
output = []
for i in range(tcase):
    slen = int(input().rstrip())
    string = input().rstrip()
    code = string[0]
    for j in range(1,slen):
        if string[j] != code[len(code) - 1]:
            code = code + string[j]
    if len(code) == 1:
        #print("0")
        output.append(0)
    elif len(code) >= 2:
        output.append(math.floor(len(code)/2))
        
for i in output:
    print(i)
