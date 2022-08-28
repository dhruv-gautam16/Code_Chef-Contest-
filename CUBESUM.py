import math
# import sys
# sys.stdout = open('./output.txt', 'w')
# sys.stdin = open('./input.txt', 'r')


def answer_finder():
    x,y,z = [int(x) for x in input().split()]
    arr = [[] for _ in range(x)]
    for idx in range(x*y):
        temp = [int(x) for x in input().split()]
        row = math.floor(idx/y)
        arr[row].append(temp)
    
    for i in range(x-1, 0, -1):
        for j in range(y):
            for k in range(z):
                arr[i][j][k] -= arr[i-1][j][k]

    for i in range(x):
        for j in range(y-1,0,-1):
            for k in range(z):
                arr[i][j][k] -= arr[i][j-1][k]

    for i in range(x):
        for j in range(y):
            for k in range(z-1, 0, -1):
                arr[i][j][k] -= arr[i][j][k-1]
    
    for i in range(x):
        for j in range(y):
            print(' '.join([str(t) for t in arr[i][j]]))


    
    


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
