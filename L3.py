import math
import copy


def prime(n):
    for j in range(2, int(math.sqrt(n)) + 1):
        if n % j == 0:
            return False 
    if n == 0 or n == 1:
        return False
    return True

t = int(input())
for _ in range(t):
    done = False
    n = list(input())
    copyNum = copy.copy(n)
    for index in range(len(copyNum)):
        if copyNum[index] == '?':
            copyNum[index] = '1'
    #"???31?" => "111311"
 
    for index in range(len(copyNum)):
        if n[index] == '?':
            if index == 0:
                start = 1 
            else:
                start = 0
          
            for digit in range(start, 10):
                character = chr(digit + 48)
                copyNum[index] = character
                newNum = int("".join(copyNum))
                #print(newNum)
                if prime(newNum):
                    print(newNum)
                    done = True 
                    break
            if done:
                break