# cook your dish here
testCases = int(input())
for i in range(testCases):
    stringData = str(input())
    countOfOne = stringData.count('1')
    countOfZero = stringData.count('0')
    if (len(stringData) % 2 == 1 or countOfZero == 0 or countOfOne == 0):
        difference = -1
    else:
        difference = abs(countOfOne-countOfZero)//2
    print(difference)
