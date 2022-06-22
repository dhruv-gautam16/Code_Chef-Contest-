
T = int(input())
for i in range(T):
    A, B = map(str, input().split(" "))
    n = int(input()) #number of children
    X = A+B
    x_dict,y_dict = {},{}
    for s in X:
        if s not in x_dict.keys():
            x_dict[s] = 1
        else:
            x_dict[s] += 1
    Y = ""
    for i in range(n):
        Y+= str(input())
    for s in Y:
        if s not in y_dict.keys():
            y_dict[s] = 1
        else:
            y_dict[s] += 1

    present = True

    for x in y_dict.keys():
        if x not in x_dict.keys():
            present = False
            break
    if not present:
        print("NO")
        continue
    truth = []
    
    for k in y_dict.keys():
        if x_dict[k] >= y_dict[k]:
            truth.append(True)
        else:
            truth.append(False)
    if all(truth):
        print("YES")
    else:
        print("NO")
