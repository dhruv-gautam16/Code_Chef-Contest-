# cook your dish here
# cook your dish here
import sys
def printAnswer(color):
    print(2)
    print(color)

print(1)
print(3,1,2,2) #pan1
print(3,3,4,4) #pan2
sys.stdout.flush()
ans = int(input())
if ans == 1:
    printAnswer(1)
elif ans == 2:
    printAnswer(2)
elif ans == -1:
    printAnswer(3)
elif ans == -2:
    printAnswer(4)
elif  ans == 0:
    printAnswer(5)
