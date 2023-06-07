# cook your dish here
def solve(b, a):
    # find the minimum of b/2 and a
    # since Chef can only make as many chaats as there are apples
    m = min(b//2, a)
    # each chaat requires 2 bananas and 1 apple
    # so the maximum number of chaats that can be made is m
    return  m

# read the number of test cases
t = int(input())

# process each test case
for i in range(t):
    # read the input values
    b, a = map(int, input().split())
    # solve the problem and print the result
    print(solve(b, a))