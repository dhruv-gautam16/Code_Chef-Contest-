cases = int(input())
for i in range(cases):
    num = int(input())
    array = [1]
    for i in range(1, num):
        array.append(i)
    add = pow(2, num)
    req = add - sum(array)
    array.append(req)
    for i in array:
        print(i, end = ' ')
    print()