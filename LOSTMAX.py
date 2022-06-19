# cook your dish here
noOfTestCases = int(input())
for _ in range(noOfTestCases):
    nPlus1 = list(map(int, input().split()))
    nPlus1.remove(len(nPlus1)-1)
    print(max(nPlus1))